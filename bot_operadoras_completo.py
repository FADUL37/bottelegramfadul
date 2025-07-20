import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = '8180765503:AAF06Y9Dmi3URSN1Uj5QQxmN6AKfvriXKKg'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔹 ARESNET", callback_data="menu_aresnet")],
        [InlineKeyboardButton("🔹 BRASILINK", callback_data="menu_brasilink")],
        [InlineKeyboardButton("🔹 CAPITAL", callback_data="menu_capital")],
        [InlineKeyboardButton("🔹 NETCENTER", callback_data="menu_netcenter")],
        [InlineKeyboardButton("🔹 LASERNET", callback_data="menu_lasernet")],
        [InlineKeyboardButton("🔹 MEGANETS", callback_data="menu_meganets")],
        [InlineKeyboardButton("🔹 MUTUM", callback_data="menu_mutum")],
        [InlineKeyboardButton("🔹 DKIROS", callback_data="menu_dkiros")],
        [InlineKeyboardButton("🔹 SETTE", callback_data="menu_sette")],
        [InlineKeyboardButton("🔹 VIVAS", callback_data="menu_vivas")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Olá! Escolha uma operadora para consultar:", reply_markup=reply_markup)

async def menu_aresnet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📶 Planos", callback_data="aresnet_planos")],
        [InlineKeyboardButton("🌍 Cobertura", callback_data="aresnet_cobertura")],
        [InlineKeyboardButton("🛠️ Equipamentos", callback_data="aresnet_equipamentos")],
        [InlineKeyboardButton("🔧 Suporte", callback_data="aresnet_suporte")],
        [InlineKeyboardButton("💰 Financeiro", callback_data="aresnet_financeiro")],
        [InlineKeyboardButton("📞 Atendimento", callback_data="aresnet_atendimento")],
        [InlineKeyboardButton("🔄 Reset", callback_data="aresnet_reset")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")],
    ]
    await query.edit_message_text("📡 *ARESNET - Selecione uma opção:*", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def menu_brasilink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📶 Planos", callback_data="brasilink_planos")],
        [InlineKeyboardButton("🌍 Cobertura", callback_data="brasilink_cobertura")],
        [InlineKeyboardButton("🛠️ Equipamentos", callback_data="brasilink_equipamentos")],
        [InlineKeyboardButton("🔧 Suporte", callback_data="brasilink_suporte")],
        [InlineKeyboardButton("💰 Financeiro", callback_data="brasilink_financeiro")],
        [InlineKeyboardButton("📞 Atendimento", callback_data="brasilink_atendimento")],
        [InlineKeyboardButton("🔄 Reset", callback_data="brasilink_reset")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")],
    ]
    await query.edit_message_text("🌐 *BRASILINK - Selecione uma opção:*", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def menu_capital(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📶 Planos", callback_data="capital_planos")],
        [InlineKeyboardButton("🌍 Cobertura", callback_data="capital_cobertura")],
        [InlineKeyboardButton("🛠️ Equipamentos", callback_data="capital_equipamentos")],
        [InlineKeyboardButton("🔧 Suporte", callback_data="capital_suporte")],
        [InlineKeyboardButton("💰 Financeiro", callback_data="capital_financeiro")],
        [InlineKeyboardButton("📞 Atendimento", callback_data="capital_atendimento")],
        [InlineKeyboardButton("🔄 Reset", callback_data="capital_reset")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")],
    ]
    await query.edit_message_text("💼 *CAPITAL FIBRA - Selecione uma opção:*", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def menu_netcenter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📶 Planos", callback_data="netcenter_planos")],
        [InlineKeyboardButton("🌍 Cobertura", callback_data="netcenter_cobertura")],
        [InlineKeyboardButton("🛠️ Equipamentos", callback_data="netcenter_equipamentos")],
        [InlineKeyboardButton("🔧 Suporte", callback_data="netcenter_suporte")],
        [InlineKeyboardButton("💰 Financeiro", callback_data="netcenter_financeiro")],
        [InlineKeyboardButton("📞 Atendimento", callback_data="netcenter_atendimento")],
        [InlineKeyboardButton("🔄 Reset", callback_data="netcenter_reset")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")],
    ]
    await query.edit_message_text("🌐 *NETCENTER - Selecione uma opção:*", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def menu_lasernet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📶 Planos", callback_data="lasernet_planos")],
        [InlineKeyboardButton("🌍 Cobertura", callback_data="lasernet_cobertura")],
        [InlineKeyboardButton("🛠️ Equipamentos", callback_data="lasernet_equipamentos")],
        [InlineKeyboardButton("🔧 Suporte", callback_data="lasernet_suporte")],
        [InlineKeyboardButton("💰 Financeiro", callback_data="lasernet_financeiro")],
        [InlineKeyboardButton("📞 Atendimento", callback_data="lasernet_atendimento")],
        [InlineKeyboardButton("🔄 Reset", callback_data="lasernet_reset")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")],
    ]
    await query.edit_message_text("🔥 *LASERNET - Selecione uma opção:*", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def menu_meganets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📶 Planos", callback_data="meganets_planos")],
        [InlineKeyboardButton("🌍 Cobertura", callback_data="meganets_cobertura")],
        [InlineKeyboardButton("🛠️ Equipamentos", callback_data="meganets_equipamentos")],
        [InlineKeyboardButton("🔧 Suporte", callback_data="meganets_suporte")],
        [InlineKeyboardButton("💰 Financeiro", callback_data="meganets_financeiro")],
        [InlineKeyboardButton("📞 Atendimento", callback_data="meganets_atendimento")],
        [InlineKeyboardButton("🔄 Reset", callback_data="meganets_reset")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")],
    ]
    await query.edit_message_text("⚡ *MEGANETS - Selecione uma opção:*", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def menu_mutum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📶 Planos", callback_data="mutum_planos")],
        [InlineKeyboardButton("🌍 Cobertura", callback_data="mutum_cobertura")],
        [InlineKeyboardButton("🛠️ Equipamentos", callback_data="mutum_equipamentos")],
        [InlineKeyboardButton("🔧 Suporte", callback_data="mutum_suporte")],
        [InlineKeyboardButton("💰 Financeiro", callback_data="mutum_financeiro")],
        [InlineKeyboardButton("📞 Atendimento", callback_data="mutum_atendimento")],
        [InlineKeyboardButton("🔄 Reset", callback_data="mutum_reset")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")],
    ]
    await query.edit_message_text("🏔️ *MUTUM - Selecione uma opção:*", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def menu_dkiros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📶 Planos", callback_data="dkiros_planos")],
        [InlineKeyboardButton("🌍 Cobertura", callback_data="dkiros_cobertura")],
        [InlineKeyboardButton("🛠️ Equipamentos", callback_data="dkiros_equipamentos")],
        [InlineKeyboardButton("🔧 Suporte", callback_data="dkiros_suporte")],
        [InlineKeyboardButton("💰 Financeiro", callback_data="dkiros_financeiro")],
        [InlineKeyboardButton("📞 Atendimento", callback_data="dkiros_atendimento")],
        [InlineKeyboardButton("🔄 Reset", callback_data="dkiros_reset")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")],
    ]
    await query.edit_message_text("🚀 *DKIROS - Selecione uma opção:*", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def menu_sette(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📶 Planos", callback_data="sette_planos")],
        [InlineKeyboardButton("🌍 Cobertura", callback_data="sette_cobertura")],
        [InlineKeyboardButton("🛠️ Equipamentos", callback_data="sette_equipamentos")],
        [InlineKeyboardButton("🔧 Suporte", callback_data="sette_suporte")],
        [InlineKeyboardButton("💰 Financeiro", callback_data="sette_financeiro")],
        [InlineKeyboardButton("📞 Atendimento", callback_data="sette_atendimento")],
        [InlineKeyboardButton("🔄 Reset", callback_data="sette_reset")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")],
    ]
    await query.edit_message_text("7️⃣ *SETTE - Selecione uma opção:*", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def menu_vivas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("📶 Planos", callback_data="vivas_planos")],
        [InlineKeyboardButton("🌍 Cobertura", callback_data="vivas_cobertura")],
        [InlineKeyboardButton("🛠️ Equipamentos", callback_data="vivas_equipamentos")],
        [InlineKeyboardButton("🔧 Suporte", callback_data="vivas_suporte")],
        [InlineKeyboardButton("💰 Financeiro", callback_data="vivas_financeiro")],
        [InlineKeyboardButton("📞 Atendimento", callback_data="vivas_atendimento")],
        [InlineKeyboardButton("🔄 Reset", callback_data="vivas_reset")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")],
    ]
    await query.edit_message_text("🌟 *VIVAS - Selecione uma opção:*", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# Função para exibir menu de mensagens prontas
async def menu_mensagens_prontas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    try:
        with open("mensagem prontas.txt", "r", encoding="utf-8") as f:
            mensagens = f.read().strip().split("\n")
        
        keyboard = []
        for i, mensagem in enumerate(mensagens, 1):
            if mensagem.strip():  # Verifica se a linha não está vazia
                # Limita o texto do botão para não ficar muito longo
                texto_botao = mensagem[:50] + "..." if len(mensagem) > 50 else mensagem
                keyboard.append([InlineKeyboardButton(f"{i}. {texto_botao}", callback_data=f"msg_pronta_{i}")])
        
        keyboard.append([InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            "📝 *MENSAGENS PRONTAS - Selecione uma mensagem:*", 
            reply_markup=reply_markup, 
            parse_mode="Markdown"
        )
    except Exception as e:
        await query.edit_message_text(
            "❌ Erro ao carregar mensagens prontas. Tente novamente.", 
            parse_mode="Markdown"
        )

# Função para exibir mensagem pronta selecionada
async def exibir_mensagem_pronta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    
    try:
        # Extrai o número da mensagem do callback_data
        numero_msg = int(data.split("_")[-1])
        
        with open("mensagem prontas.txt", "r", encoding="utf-8") as f:
            mensagens = f.read().strip().split("\n")
        
        if 1 <= numero_msg <= len(mensagens):
            mensagem_selecionada = mensagens[numero_msg - 1]
            
            keyboard = [
                [InlineKeyboardButton("📋 Copiar Mensagem", callback_data=f"copiar_msg_{numero_msg}")],
                [InlineKeyboardButton("⬅️ Voltar às Mensagens", callback_data="menu_mensagens_prontas")],
                [InlineKeyboardButton("🏠 Menu Principal", callback_data="voltar_menu")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(
                f"📝 *Mensagem Pronta #{numero_msg}:*\n\n{mensagem_selecionada}", 
                reply_markup=reply_markup, 
                parse_mode="Markdown"
            )
        else:
            await query.edit_message_text(
                "❌ Mensagem não encontrada.", 
                parse_mode="Markdown"
            )
    except Exception as e:
        await query.edit_message_text(
            "❌ Erro ao carregar mensagem. Tente novamente.", 
            parse_mode="Markdown"
        )

# Função para "copiar" mensagem (exibe novamente para facilitar cópia)
async def copiar_mensagem_pronta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("Mensagem exibida para cópia!")
    data = query.data
    
    try:
        # Extrai o número da mensagem do callback_data
        numero_msg = int(data.split("_")[-1])
        
        with open("mensagem prontas.txt", "r", encoding="utf-8") as f:
            mensagens = f.read().strip().split("\n")
        
        if 1 <= numero_msg <= len(mensagens):
            mensagem_selecionada = mensagens[numero_msg - 1]
            
            keyboard = [
                [InlineKeyboardButton("⬅️ Voltar às Mensagens", callback_data="menu_mensagens_prontas")],
                [InlineKeyboardButton("🏠 Menu Principal", callback_data="voltar_menu")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            # Envia a mensagem como texto simples para facilitar a cópia
            await query.edit_message_text(
                f"📋 *Copie a mensagem abaixo:*\n\n`{mensagem_selecionada}`", 
                reply_markup=reply_markup, 
                parse_mode="Markdown"
            )
    except Exception as e:
        await query.edit_message_text(
            "❌ Erro ao processar mensagem. Tente novamente.", 
            parse_mode="Markdown"
        )

# Função para voltar ao menu principal
async def voltar_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("🔹 ARESNET", callback_data="menu_aresnet")],
        [InlineKeyboardButton("🔹 BRASILINK", callback_data="menu_brasilink")],
        [InlineKeyboardButton("🔹 CAPITAL", callback_data="menu_capital")],
        [InlineKeyboardButton("🔹 NETCENTER", callback_data="menu_netcenter")],
        [InlineKeyboardButton("🔹 LASERNET", callback_data="menu_lasernet")],
        [InlineKeyboardButton("🔹 MEGANETS", callback_data="menu_meganets")],
        [InlineKeyboardButton("🔹 MUTUM", callback_data="menu_mutum")],
        [InlineKeyboardButton("🔹 DKIROS", callback_data="menu_dkiros")],
        [InlineKeyboardButton("🔹 SETTE", callback_data="menu_sette")],
        [InlineKeyboardButton("🔹 VIVAS", callback_data="menu_vivas")],
        [InlineKeyboardButton("📝 MENSAGENS PRONTAS", callback_data="menu_mensagens_prontas")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("👋 Olá! Escolha uma operadora para consultar ou acesse as mensagens prontas:", reply_markup=reply_markup)

async def resposta_operadora(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    try:
        with open("respostas_operadoras.txt", "r", encoding="utf-8") as f:
            linhas = f.read().split("---\n")
            respostas = {linha.split("::")[0].strip(): linha.split("::")[1].strip() for linha in linhas if "::" in linha}

        resposta = respostas.get(data, "❌ Opção inválida ou informação não disponível.")
        
        # Adiciona botão de voltar nas respostas
        keyboard = [[InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(resposta, reply_markup=reply_markup, parse_mode="Markdown")
    except Exception as e:
        await query.edit_message_text("❌ Erro ao carregar informações. Tente novamente.", parse_mode="Markdown")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # Handlers de comandos
    app.add_handler(CommandHandler("start", start))
    
    # Handlers de menus das operadoras
    app.add_handler(CallbackQueryHandler(menu_aresnet, pattern="^menu_aresnet$"))
    app.add_handler(CallbackQueryHandler(menu_brasilink, pattern="^menu_brasilink$"))
    app.add_handler(CallbackQueryHandler(menu_capital, pattern="^menu_capital$"))
    app.add_handler(CallbackQueryHandler(menu_netcenter, pattern="^menu_netcenter$"))
    app.add_handler(CallbackQueryHandler(menu_lasernet, pattern="^menu_lasernet$"))
    app.add_handler(CallbackQueryHandler(menu_meganets, pattern="^menu_meganets$"))
    app.add_handler(CallbackQueryHandler(menu_mutum, pattern="^menu_mutum$"))
    app.add_handler(CallbackQueryHandler(menu_dkiros, pattern="^menu_dkiros$"))
    app.add_handler(CallbackQueryHandler(menu_sette, pattern="^menu_sette$"))
    app.add_handler(CallbackQueryHandler(menu_vivas, pattern="^menu_vivas$"))
    
    # Handler para mensagens prontas
    app.add_handler(CallbackQueryHandler(menu_mensagens_prontas, pattern="^menu_mensagens_prontas$"))
    app.add_handler(CallbackQueryHandler(exibir_mensagem_pronta, pattern="^msg_pronta_\\d+$"))
    app.add_handler(CallbackQueryHandler(copiar_mensagem_pronta, pattern="^copiar_msg_\\d+$"))
    
    # Handler para voltar ao menu
    app.add_handler(CallbackQueryHandler(voltar_menu, pattern="^voltar_menu$"))
    
    # Handler geral para respostas (deve ser o último)
    app.add_handler(CallbackQueryHandler(resposta_operadora))

    print("🤖 Bot rodando com todas as operadoras...")
    app.run_polling()
