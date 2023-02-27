require 'liquid'

module Jekyll
  module FileFilters
    def file_exists(file)
      path = File.join(Dir.getwd, file)
      return File.file?(path) ? file : nil
    end

    def file_read(file)
      path = File.join(Dir.getwd, file)
      return File.file?(path) ? File.read(path) : nil
    end
  end
end

Liquid::Template.register_filter(Jekyll::FileFilters)
