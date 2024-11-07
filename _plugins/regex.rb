require 'liquid'

module Jekyll
  module RegexFilters
    # search string for regex capture group, return first or all matches
    def regex_scan(string, search, multi = false, all = false)
      regex = multi ? /#{search}/m : /#{search}/
      matches = string.scan(regex).flatten
      if matches.length
        return all ? matches : matches[0]
      else
        return ""
      end
    end

    # find regex capture group in string and replace 
    def regex_replace(string, search, replace)
      return string.gsub(/#{search}/m, replace)
    end

    # strip all non-letter and non-number characters from string
    def regex_strip(string)
      return string.gsub(/[^\p{L}\p{N}.,;:-]/u, " ").gsub(/\s+/, " ").strip
    end
  end
end

Liquid::Template.register_filter(Jekyll::RegexFilters)
