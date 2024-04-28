import asyncio
from aiogram import Bot, Dispatcher
import user_handlers
import comand_handlers
from env import BOT_TOKEN
from keyboards import set_main_menu

# Функция конфигурирования и запуска бота
async def main():
    # await init_models()
    bot = Bot(token=BOT_TOKEN,
              parse_mode='HTML')
    dp = Dispatcher()

    # Настраиваем главное меню бота
    await set_main_menu(bot)

    # Регистрируем роутеры в диспетчере
    dp.include_router(comand_handlers.command_router)
    dp.include_router(user_handlers.user_router)
    # metadata.drop_all(engine)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
