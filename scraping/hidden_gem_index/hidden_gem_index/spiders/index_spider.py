import scrapy


class IndexSpiderSpider(scrapy.Spider):
    name = "index_spider"
    allowed_domains = ["numbeo.com"]
    start_urls = [
                "https://www.numbeo.com/cost-of-living/rankings_current.jsp?displayColumn=2",
                "https://www.numbeo.com/quality-of-life/rankings_current.jsp?displayColumn=1",
                "https://www.numbeo.com/quality-of-life/rankings_current.jsp?displayColumn=2",
                "https://www.numbeo.com/quality-of-life/rankings_current.jsp?displayColumn=3",
                "https://www.numbeo.com/quality-of-life/rankings_current.jsp?displayColumn=5",
                "https://www.numbeo.com/quality-of-life/rankings_current.jsp?displayColumn=6",
                "https://www.numbeo.com/quality-of-life/rankings_current.jsp?displayColumn=7"
                  ]

    url_mappings = {
        'cost-of-living/rankings_current.jsp?displayColumn=2': 'cost_of_living_plus_rent_index',
        'displayColumn=1': 'purchasing_power_index',
        'quality-of-life/rankings_current.jsp?displayColumn=2' : 'safety_index',
        'displayColumn=3': 'health_care_index',
        'displayColumn=5': 'property_price_to_income_ratio',
        'displayColumn=6': 'traffic_index',
        'displayColumn=7': 'pollution_index',
    }

    def parse(self, response):

        index_name = "unknown_index"

        for key, name in self.url_mappings.items():
            if key in response.url:
                index_name = name
                break

        table = response.css('table')[1]
        rows = table.css('tr')[1:]

        for row in rows:
            country = row.css('td.cityOrCountryInIndicesTable a::text').get()
            index = row.css('td::text').get()

            if country and index:
                yield {
                    "country": country.strip(),
                    index_name: float(index.strip())
                }
