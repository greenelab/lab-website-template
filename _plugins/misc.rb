require 'liquid'
require 'html-proofer'

module Jekyll
  module MiscFilters
    # fallback if value unspecified
    def is_nil(value, fallback)
      return value == nil ? fallback : value
    end

    # get list of hash keys or array entries
    def object_items(object)
      if object.is_a?(Hash)
        return object.keys
      elsif object.is_a?(Array)
        return object
      end
      return object
    end

    # filter a list of hashes by comma-sep'd field:value pairs
    def data_filter(data, filters)
      if not data.is_a?(Array) or not filters.is_a?(String)
        return data
      end
      data = data.clone
      for filter in array_filter(filters.split(","))
        key, value = array_filter(filter.split(":"))
        # find unspecified fields
        if value == nil
          data.select!{|d| d[key] == nil}
        # find fields that match regex
        elsif value.is_a?(String)
          data.select!{|d| d[key].to_s =~ /#{value}/m}
        end
      end
      return data
    end

    # from css text, find font family definitions and construct google font url
    def google_fonts(css)
      names = regex_scan(css, '--\S*:\s*"(.*)",?.*;', false, true).sort.uniq
      weights = regex_scan(css, '--\S*:\s(\d{3});', false, true).sort.uniq
      url = "https://fonts.googleapis.com/css2?display=swap&"
      for name in names do
        name.sub!" ", "+"
        url += "&family=#{name}:ital,wght@"
        for ital in [0, 1] do
          for weight in weights do
            url += "#{ital},#{weight};"
          end
        end
        url.delete_suffix!(";")
      end
      return url
    end
  end

  # based on https://github.com/episource/jekyll-html-proofer
  module HtmlProofer
    priority = Jekyll::Hooks::PRIORITY_MAP[:high] + 1000

    Jekyll::Hooks.register(:site, :post_write, priority: priority) do |site|
      if not site.config["proofer"] == false
        options = {
          allow_missing_href: true,
          enforce_https: false,
          ignore_files: [/.*testbed.html/],
          ignore_urls: [
            /fonts\.gstatic\.com/,
            /localhost:/,
            /0\.0\.0\.0:/,
          ],
        }

        begin
          HTMLProofer.check_directory(site.dest, options).run
        rescue Exception => error
          STDERR.puts error
          # raise error
        end
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::MiscFilters)
