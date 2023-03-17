require 'liquid'

module Jekyll
  module MiscFilters
    def is_nil(value, fallback)
      return value == nil ? fallback : value
    end

    def data_filter(data, filters)
      if not data.is_a?(Array) or not filters.is_a?(String)
        return data
      end
      data = data.clone
      for filter in array_filter(filters.split(","))
        key, value = array_filter(filter.split(":"))
        if value == nil
          data.select!{|d| d[key] == nil}
        elsif value.is_a?(String)
          data.select!{|d| d[key].to_s =~ /#{value}/m}
        end
      end
      return data
    end

    def google_fonts(css)
      names = regex_scan(css, '--\S*:\s*"(.*)",?.*;', true).sort.uniq
      weights = regex_scan(css, '--\S*:\s(\d{3});', true).sort.uniq
      string = "https://fonts.googleapis.com/css2?display=swap&"
      for name in names do
        name.sub!" ", "+"
        string += "&family=#{name}:ital,wght@"
        for ital in [0, 1] do
          for weight in weights do
            string += "#{ital},#{weight};"
          end
        end
        string.delete_suffix!(";")
      end
      return string
    end
  end
end

Liquid::Template.register_filter(Jekyll::MiscFilters)
