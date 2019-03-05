_autor_ = 'yuri'

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader

#problema: extraer informacion

class Lugar(Item):
    lugar = Field()
    id = Field()

class TelaSpider(Spider):
    name = "primero tela"
    start_urls = ['https://sp.booking.com/searchresults.es-ar.html?aid=1172825;label=47801694;sid=39bdc9c8abdf1b725c40e26201e0b3de;city=-360150&class_interval=1&dest_id=-360150&dest_type=city&dtdisc=0&inac=0&index_postcard=0&keep_landing=1&label_click=undef&offset=0&postcard=0&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&ss_all=0&ssb=empty&sshis=0&utm_campaign=search-extension&utm_source=minube&']
    def parse(self, response):
        sel = Selector(response)
        lugares = sel.xpath('//div[@id=hotellist_inner]/div')

        #vamos a iterar sobre todas las preguntas

        for i, elem in enumerate(lugares):
            item = ItemLoader(Lugar(), elem)
            item.add_xpath('lugar', './/h3/a/span/text()')
            item.add_value('id',i)
            yield item.load_item()
