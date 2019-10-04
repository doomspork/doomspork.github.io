require "json"
require 'nokogiri'

class SeancallanDotCom < Jekyll::Generator
  
  def generate(site)
    
    writings = []
    site.posts.docs.each do |page|
      writings.push({
        url: "#{site.config['url']}#{page.url}",
        title: page.data['title'],
        date: page.data['date'],
        summary: page.data['excerpt']
      })
    end
    site.pages.each do |page|
      if page.name == 'writings.html'
        page.data['links'].each do |link|
          writings.push({
            url: link['url'],
            title: link['title'],
            date: link['date'],
            summary: link['summary'],
            target: "_blank"
          })
        end # do link
      end # if page.name
    end # if page.name
    site.config['writings'] = JSON.parse(writings.to_json)
  end # method
end # class

module Jekyll
  module AssetFilter
    def first_paragraph(html)
      paragraph = Nokogiri::HTML(html).css('p').first.to_html
    end
  end
end

Liquid::Template.register_filter(Jekyll::AssetFilter)