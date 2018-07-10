import scrapy

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	start_urls = [
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]

	def parse(self,response):
		for site in  response.xpath('//div[@class="title-and-desc"]/a'):
			yield {
       	 		'name': site.xpath("div/text()").extract_first(),
        		'url': site.xpath("@href").extract_first() 
    		}
