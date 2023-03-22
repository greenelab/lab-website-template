require 'liquid'

module Jekyll
  module RegexFilters
    def regex_scan(string, search, multi = false, all = false)
      regex = multi ? /#{search}/m : /#{search}/
      matches = string.scan(regex).flatten
      if matches.length
        return all ? matches : matches[0]
      else
        return ""
      end
    end

    def regex_replace(string, search, replace)
      return string.gsub(/#{search}/m, replace)
    end

    def regex_strip(string)
      return string.gsub(/[^\p{L}\p{N}]/u, " ")
    end
  end
end

Liquid::Template.register_filter(Jekyll::RegexFilters)
