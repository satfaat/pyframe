import lume from "lume/mod.ts";
import attributes from "lume/plugins/attributes.ts";
import base_path from "lume/plugins/base_path.ts";
import code_highlight from "lume/plugins/code_highlight.ts";
import date from "lume/plugins/date.ts";
import esbuild from "lume/plugins/esbuild.ts";
import eta from "lume/plugins/eta.ts";
import filter_pages from "lume/plugins/filter_pages.ts";
import imagick from "lume/plugins/imagick.ts";
import inline from "lume/plugins/inline.ts";
import jsx from "lume/plugins/jsx.ts";

const site = lume();

site.use(attributes());
site.use(base_path());
site.use(code_highlight());
site.use(date());
site.use(esbuild());
site.use(eta());
site.use(filter_pages());
site.use(imagick());
site.use(inline());
site.use(jsx());

export default site;
