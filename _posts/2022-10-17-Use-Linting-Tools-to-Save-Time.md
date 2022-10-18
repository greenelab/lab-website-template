---
title: "Tip of the Week: Use Linting Tools to Save Time"
author: Dave Bunten
member: dave-bunten
tags:
  - tip-of-the-week
  - linting
  - static-analysis
  - software
---

# Tip of the Week: Use Linting Tools to Save Time

> Each week we seek to provide a software tip of the week geared towards helping you achieve your software goals. If you have any software questions or suggestions for an upcoming tip of the week, please don’t hesitate to reach out to #software-engineering on Slack or email DBMISoftwareEngineering at olucdenver.onmicrosoft.com

Have you ever found yourself spending hours formatting your code so it looks just right? Have you ever caught a duplicative import statement in your code? We recommend using open source __linting__ tools to help avoid common issues like these and save time.

[__Software Linting__](https://en.wikipedia.org/wiki/Lint_(software)) is the practice of detecting and sometimes automatically fixing stylistic, syntactical, or other programmatic issues. Linting usually involves installing standardized or opinionated libraries which allow you to quickly make code corrections. Using linting tools also can help you learn nuanced or unwritten intricacies of programming languages while you solve problems in your work.

__TLDR (too long, didn't read);__ Linting is a type of static analysis which can be used to instantly address many common code issues. [`isort`](https://pycqa.github.io/isort/index.html) provides automatic Python import statement linting. [`pre-commit`](<https://pre-commit.com/>) provides an easy way to test and apply isort (in addition to other linting tools) through source control workflows.

## Example: Python Code Style Linting with isort

[__Isort__](https://pycqa.github.io/isort/index.html) is a Python utility for linting package import statements (sorting, deduplication, etc). Isort may be used to automatically fix your import statements or test for their consistency. See the [isort installation documentation](https://pycqa.github.io/isort/docs/quick_start/1.-install.html) for more information on getting started.

__Before isort__

The following Python code shows a series of import statements. There are duplicate imports and the imports are a mixture of custom (possibly local), external, and built-in packages. Isort can check this code using the command: `isort <file or path> --check`.

```python
from custompkg import b, a
import numpy as np
import pandas as pd
import sys
import os
import pandas as pd
import os
```

__After isort__

Isort can fix the code automatically using the command: `isort <file or path>`. After applying the fixes, notice that all packages are alphabetized and grouped by built-in, external, and custom packages.

```python
import os
import sys

import numpy as np
import pandas as pd
from custompkg import a, b
```

## Using isort with pre-commit

[__Pre-commit__](https://pre-commit.com/) is a framework which can be used to apply linting checks and fixes as [git-hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) or the command line. Pre-commit includes existing hooks for many libraries, including isort. See the [pre-commit installation documentation](https://pre-commit.com/#install) to get started.

__Example .pre-commit-config.yaml Configuration__

The following yaml content can be used to reference isort by pre-commit. This configuration content can be expanded to many different pre-commit hooks.

```yaml
# example .pre-commit-config.yaml file leveraging isort
# See https://pre-commit.com/hooks.html for more hooks
---
repos:
  - repo: https://github.com/PyCQA/isort
    rev: 5.10.1
    hooks:
      - id: isort
```

__Example Using pre-commit Manually__

Imagine we have a file, example.py, which includes the content from _Before isort_. Running pre-commit manually on the directory files will first automatically apply isort formatting. The second time pre-commit is run there will be no issue (pre-commit resolved it automatically).

First detecting and fixing the file:

```console
% pre-commit run --all-files
isort...................................Failed
- hook id: isort
- files were modified by this hook

Fixing example.py
```

Then checking that the file was fixed:

{:.left}

```console
% pre-commit run --all-files
isort...................................Passed
```
