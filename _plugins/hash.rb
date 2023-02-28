require 'liquid'

module Jekyll
  module HashFilters
    def hash_default(hash, defaults)
      if not hash.is_a?(Hash) or not defaults.is_a?(Hash)
        return hash
      end
      defaults.each do |key, value|
        if value.include?"$VALUE"
          if hash[key].is_a?(String)
            hash[key] = value.sub"$VALUE", hash[key]
          end
        else
          if hash[key] == nil or !hash.key?(key)
            hash[key] = value
          end
        end
      end
      return hash
    end

    def hash_keys(hash)
      return hash.is_a?(Hash) ? hash.keys : []
    end
  end
end

Liquid::Template.register_filter(Jekyll::HashFilters)
