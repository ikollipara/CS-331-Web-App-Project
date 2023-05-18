{ pkgs, ... }:

{
  name = "CS 331 Web Development Project";
  # https://devenv.sh/basics/

  # https://devenv.sh/packages/
  packages = [
    pkgs.git
    pkgs.nodePackages_latest.npm
    pkgs.nodejs
    pkgs.poetry
  ];

  # https://devenv.sh/scripts/

  enterShell = ''
    git --version
    node --version
    npm --version
    poetry version
  '';

  # https://devenv.sh/languages/
  # languages.nix.enable = true;
  languages.python.enable = true;
  languages.elm.enable = true;
  languages.javascript.enable = true;
  languages.typescript.enable = true;

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";
  starship.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}
