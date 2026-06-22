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

-- 🌟 CONFIGURACIÓN ESTILO IDE PARA EL EXPLORADOR NATIVO (Netrw)
vim.g.netrw_banner = 0        -- Esconde el cartel gigante de ayuda de arriba
vim.g.netrw_liststyle = 3     -- Transforma la lista plana en un Árbol Desplegable elegante
vim.g.netrw_browse_split = 4  -- Fuerza a abrir los archivos en la ventana de edición previa
vim.g.netrw_altv = 1          -- Fuerza las divisiones verticales hacia la derecha

-- Atajos maestros
vim.keymap.set('n', '<F5>', ':w<CR>:split | terminal python %<CR>', { silent = true })
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

  -- MOTOR DE AUTOCOMPLETADO Y SNIPPETS (nvim-cmp)
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

      -- 🌟 TU MEJORA: INYECCIÓN DINÁMICA DE SNIPPETS (ANSI Colors Extendidos)
      local p = luasnip.parser.parse_snippet

      local colores = {
        black   = "0", red     = "1", green   = "2", yellow  = "3",
        blue    = "4", magenta = "5", cian    = "6", white   = "7"
      }

      local snippets_ansi = {
        p("ansireset", [[\033[0m$0]]),
        p("ansibold",  [[\033[1m$1\033[0m$0]]),
        p("ansiunder", [[\033[4m$1\033[0m$0]]),
      }

      for nombre, codigo in pairs(colores) do
        -- Texto Estándar (fg)
        table.insert(snippets_ansi, p("fg" .. nombre, [[\033[3]] .. codigo .. [[m$1\033[0m$0]]))
        -- Texto Brillante (fgb)
        table.insert(snippets_ansi, p("fg" .. nombre .. "b", [[\033[9]] .. codigo .. [[m$1\033[0m$0]]))
        -- Fondo Estándar (bg)
        table.insert(snippets_ansi, p("bg" .. nombre, [[\033[4]] .. codigo .. [[m$1\033[0m$0]]))
        -- Fondo Brillante (bgb)
        table.insert(snippets_ansi, p("bg" .. nombre .. "b", [[\033[10]] .. codigo .. [[m$1\033[0m$0]]))
      end

      luasnip.add_snippets("all", snippets_ansi)

      -- Configuración del motor de completado
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

  -- LSPCONFIG: Integración nativa moderna para Neovim
  {
    "neovim/nvim-lspconfig",
    dependencies = {
      "williamboman/mason.nvim",
      "williamboman/mason-lspconfig.nvim",
    },
    config = function()
      require("mason").setup()
      require('mason-lspconfig').setup({
        ensure_installed = { "pyright" }
      })

      if vim.lsp.config and vim.lsp.config.pyright then
        vim.lsp.config.pyright.on_attach = function(_, bufnr)
          local opts = { buffer = bufnr, silent = true }
          vim.keymap.set('n', 'gd', vim.lsp.buf.definition, opts)
          vim.keymap.set('n', 'K', vim.lsp.buf.hover, opts)
        end
        
        local capabilities = require('cmp_nvim_lsp').default_capabilities()
        vim.lsp.config.pyright.capabilities = capabilities

        vim.lsp.enable('pyright')
      end
    end
  }
})