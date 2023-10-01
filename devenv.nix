{ pkgs, ... }:

{
  packages = [
    pkgs.git
    pkgs.gh
  ];

  languages.python.enable = true;
  languages.python.venv.enable = true;
  languages.python.venv.requirements = ''
    boto3
  '';

  # See full reference at https://devenv.sh/reference/options/
}
