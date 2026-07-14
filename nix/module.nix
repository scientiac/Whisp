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
  };

  config = lib.mkIf cfg.enable {
    environment.systemPackages = [ cfg.package ];
  };
}
