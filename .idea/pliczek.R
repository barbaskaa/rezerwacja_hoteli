library("rstac")
library("terra")


library("cluster")
library("tidyr")
library("ggplot2")

stac_source = stac("https://earth-search.aws.element84.com/v1")
stac_source



stac_source |>
  stac_search(
    collections = "sentinel-2-c1-l2a",
    bbox = c(17.5, 54, 19, 54.8), # xmin, ymin, xmax, ymax (WGS84)
    datetime = "2023-01-01T00:00:00Z/2023-12-31T00:00:00Z", # RFC 3339
    limit = 10) |>
    ext_query(`eo:cloud_cover` <= 20 ) |>
  post_request() -> obrazy
obrazy

unlist(lapply(obrazy$features, \(x) x$properties$"eo:cloud_cover"))


df = items_as_sf(obrazy)
plot(sf::st_geometry(df)[8], main = "Zasięg sceny", axes = TRUE)


obrazy |>
  items_select(8) |>
  assets_select(asset_names = c ("red", "green", "blue", "nir")) |>
  assets_url() -> urls
urls

#pobranie danych do folderu

dir.create("sentinel")
rastry = file.path("sentinel", basename(urls))

for (i in seq_along(urls)) {
  download.file(urls[i], rastry[i], mode = "wb")
}

#lub wykorzystanie modułu /vsicurl/

urls = paste0("/vsicurl/", urls)
r = rast(urls)
r

#wizualizacja RGB
plotRGB(r, r = 4, g = 2, b = 1, stretch = "lin")

#przygotowanie danych
set.seed(13) #ziarno losowości
mat = values(r)
mat_omit = na.omit(mat)
nrow(mat_omit)
mdl = kmeans(mat_omit, centers = 4)
# losowanie indeksów
idx = sample(1:nrow(mat_omit), size = 10000)
head(idx)


#ramka danych
stats = cbind(mat_omit[idx, ], klaster = mdl$cluster[idx])
stats = as.data.frame(stats)
head(stats)
stats = pivot_longer(stats, cols = 1:4, names_to = "kanal", values_to = "wartosc")
stats$klaster = factor(stats$klaster)
stats$kanal = factor(stats$kanal)
head(stats)


etykiety = c("Niebieski", "Zielony", "Czerwony", "Bliska\npodczerwień")

ggplot(stats, aes(x = kanal, y = wartosc, fill = klaster)) +
  geom_boxplot(show.legend = FALSE) + scale_x_discrete(labels = etykiety) +
  xlab("Kanał") +
  ylab("Odbicie")


#korelacja Pearsona

wart_nir <- stats[stats$kanal=="B08",]
wart_nir <- wart_nir$wartosc 

wart_red <- stats[stats$kanal=="B04",]
wart_red <- wart_red$wartosc 

korelacja <- cor(wart_red, wart_nir)
korelacja

ggplot(stats, aes(kanal=="B04", kanal=="B08")) +
  geom_point(alpha=0.5, color="blue") +
  theme_minimal() +
  labs(title="Wykres rozrzutu dla kanałów czerwonego i bliskiej podczerwieni", x="Czerwony", y="Bliska podczerwień")


#obliczenie i wizualizacja wskaźnika NDVI

nir <- r[[3]]
red <- r[[4]]

ndvi <- (nir - red)/(nir + red)
plot(ndvi)
