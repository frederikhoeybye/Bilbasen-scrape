from scrapy.spiders import SitemapSpider


# Execute from Anaconda Prompt: scrapy crawl bilbasen_spider -o name.csv
# saves a csv file that can be loaded into python and manipualted

class BilbasenSpider(SitemapSpider):
    name = 'bilbasen_spider'
    DOWNLOAD_DELAY = 0.2    # 0.2 ms of delay
    sitemap_urls = ['http://www.bilbasen.dk/sitemap_carsLatest.axd']


    def parse(self, response):
            yield {
                'maerke': response.xpath('//*[@id="bannerwrapper"]/div/div[1]/header/div[1]/span[3]/a/span//text()').extract_first(),
                'model': response.xpath('//*[@id="bannerwrapper"]/div/div[1]/header/div[1]/span[4]/a/span//text()').extract_first(),
                'sub_model': response.xpath('//*[@id="bannerwrapper"]/div/div[1]/header/div[1]/span[5]/a/span//text()').extract_first(),

                'salgspris': response.xpath('//*[@id="bbVipPricePrice"]/span[2]/text()').extract_first(),
                'gennemsnitlig_salgspris': response.xpath('//*[@id="bbVipPriceAverage"]/span/span/text()').extract_first(),
                'kilometer_koert': response.xpath('normalize-space(//*[@id="bbVipMileage"]/p/span[2]//text())').extract_first(),
                'kilometer_literen': response.xpath('//*[@id="bbVipUsage"]/p/span/span[2]/text()').extract_first(),
                'braendstofstype': response.xpath('//*[@id="bbVipUsage"]/p/span/span[1]/text()').extract_first(),
				'leasing': response.xpath('//*[@id="bbPriceLabel0"]/text()').extract_first(),

				'synet': response.xpath('//*[@id="bbVipDescriptionFacts"]//li[@title="Dato for sidste syn"]/text()').extract_first(), 
				'farve': response.xpath('//*[@id="bbVipDescriptionFacts"]//li[@title="Farve"]/text()').extract_first(),
				'registreret': response.xpath('//*[@id="bbVipDescriptionFacts"]//li[@title="Dato for 1. indregistrering for denne bil"]/text()').extract_first(),
				'levering': response.xpath('//*[@id="bbVipDescriptionFacts"]//li[@title="Levering"]/text()').extract_first(),
				


				
                'aargang': response.xpath('//*[@id="bbVipYear"]/p/span[2]/text()').extract_first(),

                'url': response.request.url,

                'beskrivelse': response.xpath('normalize-space(//*[@id="bbVipDescription"]/text())').extract_first(),

                'dealer_navn': response.css('h4::text')[1].extract(),
                'adresse': response.css('div.base64Link>div::text').extract(),


                'nypris': response.css('td.selectedcar::text')[0].extract(),
                'hestrekaefter_torque': response.css('td.selectedcar::text')[1].extract(),
                '0-100kmt': response.css('td.selectedcar::text')[2].extract(),
                'tophastighed': response.css('td.selectedcar::text')[3].extract(),
                'km_l': response.css('td.selectedcar::text')[4].extract(),
                'bredde': response.css('td.selectedcar::text')[5].extract(),
                'laengde': response.css('td.selectedcar::text')[6].extract(),
                'hoejde': response.css('td.selectedcar::text')[7].extract(),
                'lasteevne': response.css('td.selectedcar::text')[8].extract(),
                'traekhjul': response.css('td.selectedcar::text')[9].extract(),
                'cylindre': response.css('td.selectedcar::text')[10].extract(),
                'ABS-bremser': response.css('td.selectedcar::text')[11].extract(),
                'max_paahaeng': response.css('td.selectedcar::text')[12].extract(),
                'airbags': response.css('td.selectedcar::text')[13].extract(),
                'esp': response.css('td.selectedcar::text')[14].extract(),
                'tank': response.css('td.selectedcar::text')[15].extract(),
                'gear': response.css('td.selectedcar::text')[16].extract(),
                'geartype': response.css('td.selectedcar::text')[17].extract(),
                'vaegt': response.css('td.selectedcar::text')[18].extract(),
                'doere': response.css('td.selectedcar::text')[19].extract(),

            }

        # ...
# DecriptionFacts work with //li[@title="..."]
# to launch shell (developer mode) type:  scrapy shell <url>. can test CSS/xpath

