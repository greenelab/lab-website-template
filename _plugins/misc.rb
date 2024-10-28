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

 
    def empty_binding
      binding
    end

    # make arbitrary string into valid ruby variable name
    def safe_var_name(name)
      return name.to_s.gsub(/[^a-z]+/i, "_").gsub(/^_|_$/, "")
    end

    # filter a list of hashes
    def data_filter(data, filter)
      if not filter.is_a?(String)
        return data
      end

      # filter data
      return data.clone.select{
        |item|
        # if jekyll doc collection, get hash of doc data
        if item.is_a? Jekyll::Document
          item = item.data
        end
        # start with empty context of local variables
        b = empty_binding
        # add item as local variable
        b.local_variable_set("item", item)
        # also set each item field as local variable when evaluating filter
        item.each do |var, val|
          b.local_variable_set(safe_var_name(var), val)
        end
        # whether to keep item
        keep = true
        while true
          begin
            # evaluate expression as true/false
            keep = !!eval(filter, b)
            break
          # if a var in expression isn't a field on item
          rescue NameError => e
            # define it and re-evaluate
            b.local_variable_set(safe_var_name(e.name), nil)
          end
        end
        # keep/discard item
        keep
      }
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
