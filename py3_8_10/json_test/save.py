import json

import config

txt = json.dumps(config.config, indent=2)

with open("./test.json", "w") as f:
    f.write(txt)