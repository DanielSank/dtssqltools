Suppose you're working on a project that uses Google App Engine and Google Cloud SQL.
You have the project's source cloned on your system at `PROJECT_ROOT/`, where
`PROJECT_ROOT` is probably something like `~/src/<project_name>`.

```
$ cd PROJECT_ROOT
$ tree

    ├── <project_name>/
    │   ├── __init__.py
    │   ├── config.yaml
    │   ├── source_file.py
    │   └── another_source_file.py
    ├── README.md
    ├── setup.cfg
    ├── setup.py
    └── etc...
```

This package expects you to have two files available in your system:

- `~/.<project name>/config.yaml`
    ```
    ---
    cloud:
        USER: "root"
        PASSWORD: ...
    local:
        USER: "root"
        PASSWORD: ...
        HOST: "localhost"
        PORT: 3306
    ```

- `~/.<project name>/auth-token.json`: This is your proxy's user account auth token.

- `PROJECT_ROOT/<project name>/config.yaml`
    ```
    ---
    INSTANCE_CONNECTION_NAME:
    ```
