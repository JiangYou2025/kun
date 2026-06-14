# 本地预览：启动 Jekyll 开发服务器（自动重建 + 实时刷新）
# 用法：在仓库根目录运行  .\scripts\serve.ps1
# 打开 http://localhost:4000/kun/
$ErrorActionPreference = 'Stop'

# 确保 Ruby 在 PATH 中（winget 安装位置）
if (-not (Get-Command ruby -ErrorAction SilentlyContinue)) {
  $env:Path = 'C:\Ruby33-x64\bin;' + $env:Path
}

# 切到仓库根目录（脚本所在目录的上一级）
Set-Location (Split-Path $PSScriptRoot -Parent)

bundle exec jekyll serve --livereload --open-url
