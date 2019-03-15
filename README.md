# ssh-config-compiler

OpenSSH version 7.3 introduced a very handy `Include` feature.
For versions of SSH that do not support this feature, you can use this script
to merge configuration files together, using `Include` statements.

## How to use
1.  Create a `~/.ssh/config_base` file, which contains:
    ```
    # SSH Configuration Base
    Include abc/config
    Include def/config
    ```
    and two corresponding files with parts of your SSH configuration.
    
    For example, `~/.ssh/abc/config`
    ```
    # SSH Configuration ABC
    ```
     and `~/.ssh/def/config`
    ```
    # SSH Configuration DEF
    ```

2.  Then run the script
    ```bash
    python compile_config.py
    ```
    This will create a `~/.ssh/config` file. It parses the `~/.ssh/config_base`
    file and copies each line into the `~/.ssh/config` file, except when an
    `Include` statement is found. Lines beginning with `Include` will be
    replaced with the contents of the referenced file.
    
    Include statements will be processed recursively, so you can `Include`
    files also in `~/.ssh/abc/config`.

3.  The resulting file `~/.ssh/config` contains the contents of the included files:
    ```
    # SSH Configuration Base
    # SSH Configuration ABC
    # SSH Configuration DEF
    ```
