-- ==========================================================
-- 1. CONFIGURACIÓN BÁSICA
-- ==========================================================
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.expandtab = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.smartindent = true
vim.opt.mouse = "a"
vim.opt.clipboard = "unnamedplus"

vim.g.mapleader = " "

-- Atajos
vim.keymap.set('n', '<F5>', ':w<CR>:split | terminal python %<CR>', { silent = true })

-- ==========================================================
-- 2. LAZY.NVIM
-- ==========================================================
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"

if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable",
    lazypath,
  })
end

vim.opt.rtp:prepend(lazypath)

require("lazy").setup({

  -- TEMA VISUAL (Tokyo Night)
  {
    "folke/tokyonight.nvim",
    lazy = false,
    priority = 1000,
    config = function()
      vim.cmd("colorscheme tokyonight-storm")
    end,
  },

  -- AUTOPAIRS: Cierre automático de caracteres
  {
    "windwp/nvim-autopairs",
    event = "InsertEnter",
    config = true
  },

  -- NEO-TREE: Tu nuevo y potente explorador de archivos
  {
    "nvim-neo-tree/neo-tree.nvim",
    branch = "v3.x",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "MunifTanjim/nui.nvim",
      "nvim-tree/nvim-web-devicons",
    },
    config = function()
      require("neo-tree").setup({
        close_if_last_window = true,
        popup_border_style = "rounded",
        enable_git_status = true,
        enable_diagnostics = true,

        filesystem = {
          filtered_items = {
            visible = true,
            hide_dotfiles = false,
            hide_gitignored = false,
          },
          follow_current_file = {
            enabled = true
          },
          hijack_netrw_behavior = "open_default",
          use_libuv_file_watcher = true,
        },

        window = {
          position = "left",
          width = 30,
        }
      })

      vim.keymap.set("n", "<C-n>", ":Neotree toggle filesystem reveal left<CR>", { silent = true })
    end
  },

  -- MOTOR DE AUTOCOMPLETADO Y SNIPPETS RESTAURADOS
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

      -- 🌟 RESTAURACIÓN: Inyección dinámica de tus 32 Snippets ANSI
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
        table.insert(snippets_ansi, p("fg" .. nombre, [[\033[3]] .. codigo .. [[m$1\033[0m$0]]))
        table.insert(snippets_ansi, p("fg" .. nombre .. "b", [[\033[9]] .. codigo .. [[m$1\033[0m$0]]))
        table.insert(snippets_ansi, p("bg" .. nombre, [[\033[4]] .. codigo .. [[m$1\033[0m$0]]))
        table.insert(snippets_ansi, p("bg" .. nombre .. "b", [[\033[10]] .. codigo .. [[m$1\033[0m$0]]))
      end
      luasnip.add_snippets("all", snippets_ansi)

      cmp.setup({
        snippet = {
          expand = function(args)
            luasnip.lsp_expand(args.body)
          end,
        },

        mapping = cmp.mapping.preset.insert({
          ["<CR>"] = cmp.mapping.confirm({ select = true }),
          ["<Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then cmp.select_next_item() else fallback() end
          end, { "i", "s" }),
          ["<S-Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then cmp.select_prev_item() else fallback() end
          end, { "i", "s" }),
        }),

        sources = cmp.config.sources({
          { name = "nvim_lsp" },
          { name = "luasnip" },
        })
      })
    end
  },

  -- LSPCONFIG NATIVO MODERNO
  {
    "neovim/nvim-lspconfig",
    dependencies = {
      "williamboman/mason.nvim",
      "williamboman/mason-lspconfig.nvim",
    },
    config = function()
      require("mason").setup()

      -- 🌟 CAMBIO: Aseguramos 'sqlls' en lugar del problemático 'sqls'
      require("mason-lspconfig").setup({
        ensure_installed = { "pyright", "sqlls" }
      })

      local capabilities = require("cmp_nvim_lsp").default_capabilities()

      -- Configuración Pyright (Python)
      vim.lsp.config("pyright", {
        capabilities = capabilities,
        on_attach = function(_, bufnr)
          local opts = { buffer = bufnr, silent = true }
          vim.keymap.set("n", "gd", vim.lsp.buf.definition, opts)
          vim.keymap.set("n", "K", vim.lsp.buf.hover, opts)
        end,
      })
      vim.lsp.enable("pyright")

      -- 🌟 CONFIGURACIÓN NUEVA: Servidor SQL basado en Node (sqlls)
      vim.lsp.config("sqlls", {
        capabilities = capabilities,
        on_attach = function(_, _)
          -- Conexión estándar nativa
        end,
      })
      vim.lsp.enable("sqlls")
    end
  }
})