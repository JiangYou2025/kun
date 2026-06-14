# 本地全量构建：把站点生成到 _site/，并把 YAML/Liquid 报错暴露出来
# 用法：在仓库根目录运行  .\scripts\build.ps1
$ErrorActionPreference = 'Stop'

# 确保 Ruby 在 PATH 中（winget 安装位置）
if (-not (Get-Command ruby -ErrorAction SilentlyContinue)) {
  $env:Path = 'C:\Ruby33-x64\bin;' + $env:Path
}

# 切到仓库根目录（脚本所在目录的上一级）
Set-Location (Split-Path $PSScriptRoot -Parent)

bundle exec jekyll build
