require 'liquid'

module Jekyll
  module HashFilters
    # merge main hash with another hash of defaults
    def hash_default(hash, defaults)
      if not hash.is_a?(Hash) or not defaults.is_a?(Hash)
        return hash
      end
      defaults.each do |key, value|
        # substitute main string into default string and set main item
        if value.is_a?(String) and value.include?"$VALUE"
          if hash[key].is_a?(String)
            hash[key] = value.sub"$VALUE", hash[key]
          end
        # set main item to default item if not defined
        else
          if hash[key] == nil or !hash.key?(key)
            hash[key] = value
          end
        end
      end
      return hash
    end
  end
end

Liquid::Template.register_filter(Jekyll::HashFilters)
