require 'liquid'

module Jekyll
  module RegexFilters
    def regex_scan(string, search, all = false)
      matches = string.scan(/#{search}/).flatten
      if matches.length
        return all ? matches : matches[0]
      else
        return ""
      end
    end

    def regex_replace(string, search, replace)
      return string.gsub(/#{search}/m, replace)
    end
  end
end

Liquid::Template.register_filter(Jekyll::RegexFilters)
