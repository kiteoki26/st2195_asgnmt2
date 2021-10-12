library(rvest)
cartable_url <- "https://en.wikipedia.org/wiki/Comma-separated_values"

car_table <- read_html(cartable_url) %>%
  html_nodes(xpath='//*[@id="mw-content-text"]/div[1]/table[2]') %>%
  html_table()


write.csv(car_table, "E:\\ST2195\\ASGNMT_2\\r_csv\\car_table.csv", row.names = FALSE)

