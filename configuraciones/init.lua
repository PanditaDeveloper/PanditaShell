-- ====================================================================
-- 1. CONFIGURACIONES BÁSICAS
-- ====================================================================
vim.opt.number = true             
vim.opt.relativenumber = true     
vim.opt.expandtab = true          
vim.opt.tabstop = 4               
vim.opt.shiftwidth = 4            
vim.opt.smartindent = true        
vim.opt.mouse = "a"               
vim.opt.clipboard = "unnamedplus" 

-- Atajo maestro para ejecutar Python con F5
vim.keymap.set('n', '<F5>', ':w<CR>:split | terminal python %<CR>', { silent = true })

-- ====================================================================
-- 2. GESTOR DE PLUGINS (Lazy.nvim)
-- ====================================================================
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git", "--branch=stable", lazypath
  })
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup({
  -- Tema Visual
  { 
    "folke/tokyonight.nvim", 
    lazy = false, 
    priority = 1000,
    config = function() vim.cmd[[colorscheme tokyonight-storm]] end
  },

  -- MASON: El instalador de LSPs
  { "williamboman/mason.nvim", config = true },
  { "williamboman/mason-lspconfig.nvim" },

  -- LSPCONFIG: Conecta Neovim con los servidores instalados
  {
    "neovim/nvim-lspconfig",
    config = function()
      local lspconfig = require('lspconfig')
      
      require('mason-lspconfig').setup({
        ensure_installed = { "pyright" } -- Instala automáticamente el cerebro de Python
      })

      -- Activar la inteligencia de Python
      lspconfig.pyright.setup({
        on_attach = function(_, bufnr)
          -- ATAJOS CLAVE DEL LSP (Modo Normal)
          local opts = { buffer = bufnr, silent = true }
          -- gd = Go to Definition (Ir a la definición de la función)
          vim.keymap.set('n', 'gd', vim.lsp.buf.definition, opts)
          -- K = Hover (Mostrar documentación de lo que estás pisando)
          vim.keymap.set('n', 'K', vim.lsp.buf.hover, opts)
        end
      })
    end
  }
})