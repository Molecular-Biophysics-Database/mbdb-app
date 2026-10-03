// Generates __fixtures__/ui_model.json from the running playground page
// (plan 3R, fieldData-review F2): the deposit `ui_model`, trimmed to the
// entities_of_interest path, so tests drive the polymorphic lookup with the
// REAL model shape instead of a hand-built tree.
//
// Usage (run from mbdb-new/, with the dev server up — `./run.sh run`):
//   node ui/components/semantic-ui/js/mbdb/forms/building-blocks/__fixtures__/generate-ui-model.mjs [url]
//
// url defaults to https://127.0.0.1:5000/playground. Re-run after a model
// change and commit the new ui_model.json.
import fs from "fs";
import path from "path";
import https from "https";
import { fileURLToPath } from "url";

const URL = process.argv[2] ?? "https://127.0.0.1:5000/playground";
const dir = path.dirname(fileURLToPath(import.meta.url));

const get = (url) =>
  new Promise((resolve, reject) => {
    https
      .get(url, { rejectUnauthorized: false }, (res) => {
        let body = "";
        res.setEncoding("utf8");
        res.on("data", (chunk) => {
          body += chunk;
        });
        res.on("end", () => resolve(body));
      })
      .on("error", reject);
  });

const extract = (html) => {
  // Playground.jinja renders data-ui-model='{{ ui_model | tojson }}'
  const match = /data-ui-model='([^']*)'/.exec(html);
  if (!match) throw new Error("data-ui-model not found in the playground page");
  return JSON.parse(match[1]);
};

// Keep only the path a test walks; resolveUiNode starts at the root.
const trim = (model) => ({
  children: {
    metadata: {
      children: {
        general_parameters: {
          children: {
            entities_of_interest:
              model.children.metadata.children.general_parameters.children
                .entities_of_interest,
          },
        },
      },
    },
  },
});

const main = async () => {
  const html = await get(URL);
  const uiModel = trim(extract(html));
  const out = path.join(dir, "ui_model.json");
  fs.writeFileSync(out, `${JSON.stringify(uiModel, null, 2)}\n`);
  process.stdout.write(`wrote ${out}\n`);
};

main().catch((error) => {
  process.stderr.write(`${error.message}\n`);
  process.exit(1);
});
