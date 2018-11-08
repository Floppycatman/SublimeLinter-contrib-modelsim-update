SublimeLinter-contrib-modelsim
================================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to `vcom`/`vlog` - VHDL/Verilog/SystemVerilog compilers provided with [ModelSim](https://www.mentor.com/products/fv/modelsim/) and QuestaSim which provide a linting mode. `vcom` will be used with "VHDL" files , `vlog` with "Verilog" and "SystemVerilog" files.

## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `vcom`/`vlog` are installed on your system.

In order for `vcom`/`vlog` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings

- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

## Passing arguments to `vcom`/`vlog`

Arguments can be passed in a [linter settings](http://www.sublimelinter.com/en/stable/linter_settings.html#args) file or set in a [project settings](http://www.sublimelinter.com/en/stable/settings.html#project-settings) file:

<ol>
<li>Using linter settings file:

```javascript
// SublimeLinter Settings - User
{
    "linters": {
        "vcom": {
            "args": ["-2008", "-lint", "-check_synthesis"],
            "working_dir": "$project_path/../sim"
        },
        "vlog": {
            "args": ["-sv", "-lint", "-check_synthesis"],
            "working_dir": "$project_path/../sim"
        }
    }
}
```
</li>
<li>Alternately, project specific arguments can be set in a project file:

```javascript
"settings": {
    // SublimeLinter-contrib-modelsim
    "SublimeLinter.linters.vcom.args": ["-2008", "-lint", "-check_synthesis"],
    "SublimeLinter.linters.vcom.working_dir": "$project_path/../sim",
    "SublimeLinter.linters.vlog.args": ["-sv", "-lint", "-check_synthesis"],
    "SublimeLinter.linters.vlog.working_dir": "$project_path/../sim"
},
```
</li>
</ol>


## Demo

`vcom` for VHDL file:

![vcom_lint_example](https://user-images.githubusercontent.com/41512424/43842022-1b0f35ac-9b2d-11e8-981b-67d98e905fa3.png)

`vlog` for Verilog file:

![vlog_lint_example](https://user-images.githubusercontent.com/41512424/43842998-3000ae58-9b2f-11e8-8dff-4023410403c4.png)
