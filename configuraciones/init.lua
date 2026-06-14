-- ====================================================================
-- 1. CONFIGURACIONES BÁSICAS (Velocidad y Comodidad)
-- ====================================================================
vim.opt.number = true             -- Muestra el número de línea actual
vim.opt.relativenumber = true     -- Números relativos (¡básico para moverte como pro!)
vim.opt.expandtab = true          -- Convierte los tabs en espacios
vim.opt.tabstop = 4               -- 1 Tabulador = 4 espacios
vim.opt.shiftwidth = 4            -- Tamaño de la indentación
vim.opt.smartindent = true        -- Auto-indentación inteligente para código
vim.opt.mouse = "a"               -- Permite usar el mouse por si acaso (clic, scroll)
vim.opt.clipboard = "unnamedplus" -- Sincroniza el portapapeles de Neovim con el de Windows

-- Atajo maestro para ejecutar Python con F5
vim.keymap.set('n', '<F5>', ':w<CR>:split | terminal python %<CR>', { silent = true })

-- Explorador de archivos Netrw (Ctrl + n abre/cierra el panel izquierdo al 25% de pantalla)
vim.keymap.set('n', '<C-n>', ':Lex 25<CR>', { silent = true })

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
  -- Tema Visual (Tokyo Night)
  { 
    "folke/tokyonight.nvim", 
    lazy = false, 
    priority = 1000,
    config = function() vim.cmd[[colorscheme tokyonight-storm]] end
  },

  -- AUTO-PAIRS: Auto-cierre de paréntesis, llaves, comillas, etc.
  {
    "windwp/nvim-autopairs",
    event = "InsertEnter",
    opts = {} 
  },

  -- MOTOR DE AUTOCOMPLETADO (nvim-cmp)
  {
    "hrsh7th/nvim-cmp",
    dependencies = {
      "hrsh7th/cmp-nvim-lsp",     
      "L3MON4D3/LuaSnip",         
      "saadparwaiz1/cmp_luasnip", 
    },
    config = function()
      local cmp = require("cmp")
      local luasnip = require("luasnip")

      cmp.setup({
        snippet = {
          expand = function(args) luasnip.lsp_expand(args.body) end,
        },
        mapping = cmp.mapping.preset.insert({
          ["<CR>"] = cmp.mapping.confirm({ select = true }),
          ["<Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_next_item()
            elseif luasnip.expand_or_jumpable() then
              luasnip.expand_or_jump()
            else
              fallback()
            end
          end, { "i", "s" }),
          ["<S-Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_prev_item()
            elseif luasnip.jumpable(-1) then
              luasnip.jump(-1)
            else
              fallback()
            end
          end, { "i", "s" }),
        }),
        sources = cmp.config.sources({
          { name = "nvim_lsp" }, 
          { name = "luasnip" },  
        })
      })
    end
  },

  -- LSPCONFIG: Encapsulado con Mason como dependencias obligatorias previas
  {
    "neovim/nvim-lspconfig",
    dependencies = {
      "williamboman/mason.nvim",
      "williamboman/mason-lspconfig.nvim",
    },
    config = function()
      -- 1. Forzamos la carga del Mason base primero
      require("mason").setup()
      
      -- 2. Forzamos la carga del puente lspconfig segundo
      require('mason-lspconfig').setup({
        ensure_installed = { "pyright" }
      })

      -- 3. Una vez listos los anteriores, levantamos Pyright de forma nativa moderna
      if vim.lsp.config and vim.lsp.config.pyright then
        vim.lsp.config.pyright.on_attach = function(_, bufnr)
          local opts = { buffer = bufnr, silent = true }
          vim.keymap.set('n', 'gd', vim.lsp.buf.definition, opts)
          vim.keymap.set('n', 'K', vim.lsp.buf.hover, opts)
        end
        
        -- Conectar capacidades del menú flotante de autocompletado
        local pcall_cmp, cmp_lsp = pcall(require, 'cmp_nvim_lsp')
        if pcall_cmp then
          vim.lsp.config.pyright.capabilities = cmp_lsp.default_capabilities()
        end

        vim.lsp.enable('pyright')
      end
    end
  }
})