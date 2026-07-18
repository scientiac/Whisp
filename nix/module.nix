inputs:
{ config, lib, pkgs, ... }:

let
  cfg = config.programs.whisp;
  defaultPackage = inputs.self.packages.${pkgs.stdenv.hostPlatform.system}.default;
in {
  options.programs.whisp = {
    enable = lib.mkEnableOption "Whisp, a minimalist, gesture-driven scratchpad for GNOME";

    package = lib.mkOption {
      type = lib.types.package;
      default = defaultPackage;
      defaultText = "inputs.self.packages.\${pkgs.stdenv.hostPlatform.system}.default";
      description = "The Whisp package to install.";
    };

    settings = lib.mkOption {
      type = lib.types.attrsOf lib.types.anything;
      default = {};
      example = {
        font_name = "VictorMono Nerd Font Bold 11";
        paper_theme = "blank";
        confirm_delete = true;
      };
      description = "Configuration options for Whisp.";
    };
  };

  config = lib.mkIf cfg.enable {
    home.packages = [ cfg.package ];

    xdg.configFile."whisp/config.json" = lib.mkIf (cfg.settings != {}) {
      text = builtins.toJSON cfg.settings;
    };
  };
}
