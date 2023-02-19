from aiogram import Bot,Dispatcher,executor,types
import pyqrcode
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from random import randint

bot = Bot("1728116444:AAFNi5AMJg_hlfVSW-IrJ4tWR84UcifxrLA")

dp = Dispatcher(bot)

# button1 = KeyboardButton("Hello!")
# button2 = KeyboardButton("Youtube")
# keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button1).add(button2)

# @dp.message_handler(commands=['start','help'])
# async def welcome(message:types.Message):
#     await message.reply("Hello! i am esral",reply_markup=keyboard1)



# button5 = InlineKeyboardButton(text="random 1-10",callback_data="randomOf10")
# button6 = InlineKeyboardButton(text="random 1-100",callback_data="randomOf100")
# keyboard3= InlineKeyboardMarkup().add(button5,button6)

# @dp.message_handler(commands=["random"])
# async def random(message:types.Message):
#     await message.reply("Select a range :",reply_markup=keyboard3)
# @dp.callback_query_handler(text= ['randomOf10','randomOf100'])
# async def random_value(call:types.CallbackQuery):
#     if call.data == "randomOf10":
#         await call.message.answer(10)
#     if call.data == "randomOf100":
#         await call.message.answer(100)
#     await call.answer()

# @dp.message_handler(commands=["logo"])
# async def logo(message:types.Message):
#     await message.answer_photo("https://avatars.githubusercontent.com/u/61075444?v=4")

@dp.message_handler()
async def echo(message:types.Message):
    car = message.text
    car = car.replace("p", "ፕ")
    car = car.replace("ፕe", "ፐ")
    car = car.replace("ፕu", "ፑ")
    car = car.replace("ፕi", "ፒ")
    car = car.replace("ፕa", "ፓ")
    car = car.replace("ፐe", "ፔ")
    car = car.replace("ፕé", "ፔ")
    car = car.replace("ፕo", "ፖ")
    car = car.replace("ፓa", "ፗ")
    await message.answer(car)

# @dp.message_handler()
# async def qr(message:types.Message):
#     text =  pyqrcode.create(message.text)
#     text.png("code.png",scale=5)
#     await bot.send_photo(chat_id=message.chat.id, photo=open('code.png','rb'))

# button3 = KeyboardButton("who r u ?",request_contact=True)
# button4 = KeyboardButton("where r u ?",request_location=True)
# keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).row(button3,button4)
# @dp.message_handler(commands=["info"])
# async def info(message:types.Message):
#     await message.reply("Say something about you",reply_markup=keyboard2)


# @dp.message_handler()
# async def kb_answer(message:types.Message):
#     if message.text == "Hello!":
#         await message.answer("HI how u doing")
#     if message.text == "Youtube":
#         await message.answer("youtube is streaming platform")
#     else:
#         await message.answer("your message is: "+message.text)
executor.start_polling(dp)










































from aiogram import Bot,Dispatcher,executor,types
import pyqrcode
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from random import randint

bot = Bot("1728116444:AAFNi5AMJg_hlfVSW-IrJ4tWR84UcifxrLA")

dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message:types.Message):
    car = message.text
    # car = car.replace("[äâ]", "e")
    # car = car.replace("[êëē]", "é")

    car = car.replace("[əǝ]", "")  #"" 601 schwa 417 inversé retrait caractère

    car = car.replace("w", "ው")
    car = car.replace("ውe", "ወ")
    car = car.replace("ውu", "ዉ")
    car = car.replace("ውi", "ዊ")
    car = car.replace("ውa", "ዋ")
    car = car.replace("ውe", "ዌ")
    car = car.replace("ውé", "ዌ")
    car = car.replace("ውo", "ዎ")

    car = car.replace("h", "ህ")
    car = car.replace("ህe", "ሀ")
    car = car.replace("ህu", "ሁ")
    car = car.replace("ህi", "ሂ")
    car = car.replace("ህa", "ሃ")
    car = car.replace("ሀe", "ሄ")
    car = car.replace("ህé", "ሄ")
    car = car.replace("ህo", "ሆ")
    car = car.replace("ሃa", "ዏ")


    car = car.replace("[Xḫẖ]", "ኅ")  #"" second carac h tiret + retrait x
    car = car.replace("ህ=", "ኅ") 
    car = car.replace("ኅe", "ኀ")
    car = car.replace("ኅu", "ኁ")
    car = car.replace("ኅi", "ኂ")
    car = car.replace("ኅa", "ኃ")
    car = car.replace("ኀe", "ኄ")
    car = car.replace("ኅé", "ኄ")
    car = car.replace("ኅo", "ኆ")
    car = car.replace("ኃa", "ኋ")

    # "" Xw
    car = car.replace("ኅው", "ኍ")
    car = car.replace("ኍe", "ኈ")
    car = car.replace("ኍi", "ኊ")
    car = car.replace("ኍa", "ኋ")
    car = car.replace("ኈe", "ኌ")
    car = car.replace("ኍé", "ኌ")

    car = car.replace("[lL]", "ል")
    car = car.replace("ልe", "ለ")
    car = car.replace("ልu", "ሉ")
    car = car.replace("ልi", "ሊ")
    car = car.replace("ልa", "ላ")
    car = car.replace("ለe", "ሌ")
    car = car.replace("ልé", "ሌ")
    car = car.replace("ልo", "ሎ")
    car = car.replace("ላa", "ሏ")

    car = car.replace("[ḥH]", "ሕ")
    car = car.replace("ሕe", "ሐ")
    car = car.replace("ሕu", "ሑ")
    car = car.replace("ሕi", "ሒ")
    car = car.replace("ሕa", "ሓ")
    car = car.replace("ሐe", "ሔ")
    car = car.replace("ሕé", "ሔ")
    car = car.replace("ሕo", "ሖ")
    car = car.replace("ሓa", "ሗ")

    car = car.replace("[mM]", "ም")
    car = car.replace("ምe", "መ")
    car = car.replace("ምu", "ሙ")
    car = car.replace("ምi", "ሚ")
    car = car.replace("ምa", "ማ")
    car = car.replace("መe", "ሜ")
    car = car.replace("ምé", "ሜ")
    car = car.replace("ምo", "ሞ")
    car = car.replace("ማa", "ሟ")
    car = car.replace("ምY", "ፙ")
    car = car.replace("ፙa", "ፙ")

    car = car.replace("r", "ር")
    car = car.replace("ርe", "ረ")
    car = car.replace("ርu", "ሩ")
    car = car.replace("ርi", "ሪ")
    car = car.replace("ርa", "ራ")
    car = car.replace("ረe", "ሬ")
    car = car.replace("ርé", "ሬ")
    car = car.replace("ርo", "ሮ")
    car = car.replace("ራa", "ሯ")
    car = car.replace("ርY", "ፘ")
    car = car.replace("ፘa", "ፘ")

    car = car.replace("s", "ስ")
    car = car.replace("ስe", "ሰ")
    car = car.replace("ስu", "ሱ")
    car = car.replace("ስi", "ሲ")
    car = car.replace("ስa", "ሳ")
    car = car.replace("ሰe", "ሴ")
    car = car.replace("ስé", "ሴ")
    car = car.replace("ስo", "ሶ")
    car = car.replace("ሳa", "ሷ")

    car = car.replace("z", "ዝ")
    car = car.replace("ዝe", "ዘ")
    car = car.replace("ዝu", "ዙ")
    car = car.replace("ዝi", "ዚ")
    car = car.replace("ዝa", "ዛ")
    car = car.replace("ዘe", "ዜ")
    car = car.replace("ዝé", "ዜ")
    car = car.replace("ዝo", "ዞ")
    car = car.replace("ዛa", "ዟ")

    # "" ś= sz
    car = car.replace("ś", "ሥ")
    car = car.replace("ስ=", "ሥ")
    car = car.replace("ስዝ", "ሥ")
    car = car.replace("ሥe", "ሠ")
    car = car.replace("ሥu", "ሡ")
    car = car.replace("ሥi", "ሢ")
    car = car.replace("ሥa", "ሣ")
    car = car.replace("ሠe", "ሤ")
    car = car.replace("ሥé", "ሤ")
    car = car.replace("ሥo", "ሦ")
    car = car.replace("ሣa", "ሧ")

    # "" sh=ss
    car = car.replace("š", "ሽ")
    car = car.replace("ስስ", "ሽ")
    car = car.replace("ስህ", "ሽ")
    car = car.replace("ሽe", "ሸ")
    car = car.replace("ሽu", "ሹ")
    car = car.replace("ሽi", "ሺ")
    car = car.replace("ሽa", "ሻ")
    car = car.replace("ሸe", "ሼ")
    car = car.replace("ሽé", "ሼ")
    car = car.replace("ሽo", "ሾ")
    car = car.replace("ሻa", "ሿ")


    car = car.replace("q", "ቅ")
    car = car.replace("ቅe", "ቀ")
    car = car.replace("ቅu", "ቁ")
    car = car.replace("ቅi", "ቂ")
    car = car.replace("ቅa", "ቃ")
    car = car.replace("ቀe", "ቄ")
    car = car.replace("ቅé", "ቄ")
    car = car.replace("ቅo", "ቆ")
    car = car.replace("ቃa", "ቋ")


    car = car.replace("ቅው", "ቍ")
    car = car.replace("ቍe", "ቈ")
    car = car.replace("ቍi", "ቊ")
    car = car.replace("ቍa", "ቋ")
    car = car.replace("ቈe", "ቌ")
    car = car.replace("ቍé", "ቌ")

    # ""qh = qq
    car = car.replace("ቅህ", "ቕ")
    car = car.replace("ቅቅ", "ቕ")
    car = car.replace("ቕe", "ቐ")
    car = car.replace("ቕu", "ቑ")
    car = car.replace("ቕi", "ቒ")
    car = car.replace("ቕa", "ቓ")
    car = car.replace("ቐe", "ቔ")
    car = car.replace("ቕé", "ቔ")
    car = car.replace("ቕo", "ቖ")


    car = car.replace("ቕው", "ቝ")
    car = car.replace("ቝe", "ቘ")
    car = car.replace("ቝi", "ቚ")
    car = car.replace("ቝa", "ቛ")
    car = car.replace("ቘe", "ቜ")
    car = car.replace("ቝé", "ቜ")



    car = car.replace("[bB]", "ብ")
    car = car.replace("ብe", "በ")
    car = car.replace("ብu", "ቡ")
    car = car.replace("ብi", "ቢ")
    car = car.replace("ብa", "ባ")
    car = car.replace("በe", "ቤ")
    car = car.replace("ብé", "ቤ")
    car = car.replace("ብo", "ቦ")
    car = car.replace("ባa", "ቧ")

    # "" v = bb
    car = car.replace("[vV]", "ቭ")
    car = car.replace("ብብ", "ቭ")
    car = car.replace("ቭe", "ቨ")
    car = car.replace("ቭu", "ቩ")
    car = car.replace("ቭi", "ቪ")
    car = car.replace("ቭa", "ቫ")
    car = car.replace("ቨe", "ቬ")
    car = car.replace("ቭé", "ቬ")
    car = car.replace("ቭo", "ቮ")
    car = car.replace("ቫa", "ቯ")

    car = car.replace("t", "ት")
    car = car.replace("ትe", "ተ")
    car = car.replace("ትu", "ቱ")
    car = car.replace("ትi", "ቲ")
    car = car.replace("ትa", "ታ")
    car = car.replace("ተe", "ቴ")
    car = car.replace("ትé", "ቴ")
    car = car.replace("ትo", "ቶ")
    car = car.replace("ታa", "ቷ")

    # ""c=tt
    car = car.replace("ትት", "ች")
    car = car.replace("[cč]", "ች")
    car = car.replace("ችe", "ቸ")
    car = car.replace("ችu", "ቹ")
    car = car.replace("ችi", "ቺ")
    car = car.replace("ችa", "ቻ")
    car = car.replace("ቸe", "ቼ")
    car = car.replace("ችé", "ቼ")
    car = car.replace("ችo", "ቾ")
    car = car.replace("ቻa", "ቿ")

    car = car.replace("n", "ን")
    car = car.replace("ንe", "ነ")
    car = car.replace("ንu", "ኑ")
    car = car.replace("ንi", "ኒ")
    car = car.replace("ንa", "ና")
    car = car.replace("ነe", "ኔ")
    car = car.replace("ንé", "ኔ")
    car = car.replace("ንo", "ኖ")
    car = car.replace("ናa", "ኗ")

    # "" ñ=ny=nn
    car = car.replace("N", "ኝ")
    car = car.replace("ñ", "ኝ")
    car = car.replace("ንy", "ኝ")
    car = car.replace("ንን", "ኝ")
    car = car.replace("ኝe", "ኘ")
    car = car.replace("ኝu", "ኙ")
    car = car.replace("ኝi", "ኚ")
    car = car.replace("ኝa", "ኛ")
    car = car.replace("ኝe", "ኜ")
    car = car.replace("ኝé", "ኜ")
    car = car.replace("ኝo", "ኞ")
    car = car.replace("ኛa", "ኟ")


    car = car.replace("k", "ክ")
    car = car.replace("ክe", "ከ")
    car = car.replace("ክu", "ኩ")
    car = car.replace("ክi", "ኪ")
    car = car.replace("ክa", "ካ")
    car = car.replace("ከe", "ኬ")
    car = car.replace("ክé", "ኬ")
    car = car.replace("ክo", "ኮ")
    car = car.replace("ካa", "ኯ")

    # ""kw
    car = car.replace("ክው", "ኵ")
    car = car.replace("ኵe", "ኰ")
    car = car.replace("ኵi", "ኲ")
    car = car.replace("ኵa", "ኳ")
    car = car.replace("ኰe", "ኴ")
    car = car.replace("ኵé", "ኴ")


    # ""x =kk
    car = car.replace("x", "ኽ")
    car = car.replace("ክክ", "ኽ")
    car = car.replace("ክኅ", "ኽ")
    car = car.replace("ኽe", "ኸ")
    car = car.replace("ኽu", "ኹ")
    car = car.replace("ኽi", "ኺ")
    car = car.replace("ኽa", "ኻ")
    car = car.replace("ኽe", "ኼ")
    car = car.replace("ኽé", "ኼ")
    car = car.replace("ኽo", "ኾ")
    # ""xw
    car = car.replace("ኽው", "ዅ")
    car = car.replace("ዅe", "ዀ")
    car = car.replace("ዅi", "ዂ")
    car = car.replace("ዅa", "ዃ")
    car = car.replace("ዀe", "ዄ")
    car = car.replace("ዅé", "ዄ")


    # ""ž=zz
    car = car.replace("[Zž]", "ዥ")
    car = car.replace("ዝዝ", "ዥ")
    car = car.replace("ዝህ", "ዥ")
    car = car.replace("ዥe", "ዠ")
    car = car.replace("ዥu", "ዡ")
    car = car.replace("ዥi", "ዢ")
    car = car.replace("ዥa", "ዣ")
    car = car.replace("ዠe", "ዤ")
    car = car.replace("ዥé", "ዤ")
    car = car.replace("ዥo", "ዦ")
    car = car.replace("ዣa", "ዧ")

    car = car.replace("y", "ይ")
    car = car.replace("ይe", "የ")
    car = car.replace("ይu", "ዩ")
    car = car.replace("ይi", "ዪ")
    car = car.replace("ይa", "ያ")
    car = car.replace("የe", "ዬ")
    car = car.replace("ይé", "ዬ")
    car = car.replace("ይo", "ዮ")
    car = car.replace("ያa", "ዯ")

    car = car.replace("d", "ድ")
    car = car.replace("ድe", "ደ")
    car = car.replace("ድu", "ዱ")
    car = car.replace("ድi", "ዲ")
    car = car.replace("ድa", "ዳ")
    car = car.replace("ደe", "ዴ")
    car = car.replace("ድé", "ዴ")
    car = car.replace("ድo", "ዶ")
    car = car.replace("ዳa", "ዷ")


    car = car.replace("[Dḍ]", "ዽ")
    car = car.replace("ዽe", "ዸ")
    car = car.replace("ዽu", "ዹ")
    car = car.replace("ዽi", "ዺ")
    car = car.replace("ዽa", "ዻ")
    car = car.replace("ዸe", "ዼ")
    car = car.replace("ዽé", "ዼ")
    car = car.replace("ዽo", "ዾ")
    car = car.replace("ዻa", "ዿ")

    # ""j=dd
    car = car.replace("[ǧjJ]", "ጅ")
    car = car.replace("ድድ", "ጅ")
    car = car.replace("ጅe", "ጀ")
    car = car.replace("ጅu", "ጁ")
    car = car.replace("ጅi", "ጂ")
    car = car.replace("ጅa", "ጃ")
    car = car.replace("ጀe", "ጄ")
    car = car.replace("ጅé", "ጄ")
    car = car.replace("ጅo", "ጆ")
    car = car.replace("ጃa", "ጇ")

    car = car.replace("g", "ግ")
    car = car.replace("ግe", "ገ")
    car = car.replace("ግu", "ጉ")
    car = car.replace("ግi", "ጊ")
    car = car.replace("ግa", "ጋ")
    car = car.replace("ገe", "ጌ")
    car = car.replace("ግé", "ጌ")
    car = car.replace("ግo", "ጎ")
    car = car.replace("ጋa", "ጓ")

    # "" gw
    # car = car.replace("ግው", "ጕ")
    # car = car.replace("ጕe", "ጐ")
    # car = car.replace("ጕi", "ጒ")
    # car = car.replace("ጕa", "ጓ")
    # car = car.replace("ጐe", "ጔ")
    # car = car.replace("ጕé", "ጔ")


    # car = car.replace("ግግ", "ጝ")
    # car = car.replace("", "ጝ")
    # car = car.replace("ጝe", "ጘ")
    # car = car.replace("ጝu", "ጙ")
    # car = car.replace("ጝi", "ጚ")
    # car = car.replace("ጝa", "ጛ")
    # car = car.replace("ጘe", "ጜ")
    # car = car.replace("ጝé", "ጜ")
    # car = car.replace("ጝo", "ጞ")
    # car = car.replace("ጛa", "ጟ")

    car = car.replace("[Tṭ]", "ጥ")
    car = car.replace("ትህ", "ጥ")
    car = car.replace("ጥe", "ጠ")
    car = car.replace("ጥu", "ጡ")
    car = car.replace("ጥi", "ጢ")
    car = car.replace("ጥa", "ጣ")
    car = car.replace("ጠe", "ጤ")
    car = car.replace("ጥé", "ጤ")
    car = car.replace("ጥo", "ጦ")
    car = car.replace("ጣa", "ጧ")

    # ""C=TT
    car = car.replace("ጥጥ", "ጭ")
    car = car.replace("[Cċ]", "ጭ")
    car = car.replace("ችህ", "ጭ")
    car = car.replace("ጭe", "ጨ")
    car = car.replace("ጭu", "ጩ")
    car = car.replace("ጭi", "ጪ")
    car = car.replace("ጭa", "ጫ")
    car = car.replace("ጨe", "ጬ")
    car = car.replace("ጭé", "ጬ")
    car = car.replace("ጭo", "ጮ")
    car = car.replace("ጫa", "ጯ")

    car = car.replace("p̣", "ጵ")
    car = car.replace("P", "ጵ")
    car = car.replace("ፕህ", "ጵ")
    car = car.replace("ጵe", "ጰ")
    car = car.replace("ጵu", "ጱ")
    car = car.replace("ጵi", "ጲ")
    car = car.replace("ጵa", "ጳ")
    car = car.replace("ጰe", "ጴ")
    car = car.replace("ጵé", "ጴ")
    car = car.replace("ጵo", "ጶ")
    car = car.replace("ጳa", "ጷ")

    car = car.replace("[Sṣ]", "ጽ")
    car = car.replace("ትስ", "ጽ")
    car = car.replace("ጽe", "ጸ")
    car = car.replace("ጽu", "ጹ")
    car = car.replace("ጽi", "ጺ")
    car = car.replace("ጽa", "ጻ")
    car = car.replace("ጸe", "ጼ")
    car = car.replace("ጽé", "ጼ")
    car = car.replace("ጽo", "ጾ")
    car = car.replace("ጻa", "ጿ")

    car = car.replace("S=", "ፅ")
    car = car.replace("ṣ́", "ፅ")
    car = car.replace("ትዝ", "ፅ")
    car = car.replace("ፅe", "ፀ")
    car = car.replace("ፅu", "ፁ")
    car = car.replace("ፅi", "ፂ")
    car = car.replace("ፅa", "ፃ")
    car = car.replace("ፀe", "ፄ")
    car = car.replace("ፅé", "ፄ")
    car = car.replace("ፅo", "ፆ")
    car = car.replace("ፃa", "ፇ")

    car = car.replace("[fF]", "ፍ")
    car = car.replace("ፍe", "ፈ")
    car = car.replace("ፍu", "ፉ")
    car = car.replace("ፍi", "ፊ")
    car = car.replace("ፍa", "ፋ")
    car = car.replace("ፈe", "ፌ")
    car = car.replace("ፍé", "ፌ")
    car = car.replace("ፍo", "ፎ")
    car = car.replace("ፋa", "ፏ")

    # "" non identif
    # ""car = car.replace("ፍY", "ፚ")
    # ""car = car.replace("ፚa", "ፚ")

    car = car.replace("p", "ፕ")
    car = car.replace("ፕe", "ፐ")
    car = car.replace("ፕu", "ፑ")
    car = car.replace("ፕi", "ፒ")
    car = car.replace("ፕa", "ፓ")
    car = car.replace("ፐe", "ፔ")
    car = car.replace("ፕé", "ፔ")
    car = car.replace("ፕo", "ፖ")
    car = car.replace("ፓa", "ፗ")

    # "" pharyngale 
    car = car.replace("ʿ", "ዕ")
    car = car.replace("\<", "ዕ")
    car = car.replace("\"", "ዕ")
    car = car.replace("ዕe", "ዐ")
    car = car.replace("ዕu", "ዑ")
    car = car.replace("ዕi", "ዒ")
    car = car.replace("ዕa", "ዓ")
    car = car.replace("ዐe", "ዔ")
    car = car.replace("ዕé", "ዔ")
    car = car.replace("ዕo", "ዖ")

    car = car.replace("E", "ዐ")
    car = car.replace("U", "ዑ")
    car = car.replace("I", "ዒ")
    car = car.replace("A", "ዓ")
    car = car.replace("ዐዐ", "ዔ")
    car = car.replace("É", "ዔ")
    car = car.replace("O", "ዖ")

    # "" glottales 
    car = car.replace("ʾ", "እ")
    car = car.replace("\>", "እ")
    car = car.replace("\'", "እ")
    car = car.replace("እe", "አ")
    car = car.replace("እu", "ኡ")
    car = car.replace("እi", "ኢ")
    car = car.replace("እa", "ኣ")
    car = car.replace("አe", "ኤ")
    car = car.replace("እé", "ኤ")
    car = car.replace("እo", "ኦ")
    car = car.replace("ኣa", "ኧ")

    car = car.replace("e", "አ")
    car = car.replace("u", "ኡ")
    car = car.replace("i", "ኢ")
    car = car.replace("a", "ኣ")
    car = car.replace("አአ", "ኤ")
    car = car.replace("é", "ኤ")
    car = car.replace("o", "ኦ")
    car = car.replace("ኣኣ", "ኧ")

    # ""ponctuation 
    car = car.replace("-", "፡")
    car = car.replace("\.", "።")
    car = car.replace("\,", "፣")
    # car = car.replace('\', '፤')
    car = car.replace("\:", "፥")
    car = car.replace("\!", "፦")
    car = car.replace("\?", "፧")
    car = car.replace("\"", "፨")

    car = car.replace("1", "፩")
    car = car.replace("2", "፪")
    car = car.replace("3", "፫")
    car = car.replace("4", "፬")
    car = car.replace("5", "፭")
    car = car.replace("6", "፮")
    car = car.replace("7", "፯")
    car = car.replace("8", "፰")
    car = car.replace("9", "፱")
    car = car.replace("፩0", "፲")
    car = car.replace("፪0", "፳")
    car = car.replace("፫0", "፴")
    car = car.replace("፬0", "፵")
    car = car.replace("፭0", "፶")
    car = car.replace("፮0", "፷")
    car = car.replace("፯0", "፸")
    car = car.replace("፰0", "፹")
    car = car.replace("፱0", "፺")
    car = car.replace("፲0", "፻")
    car = car.replace("፳0", "፪፻")
    car = car.replace("፺0", "፱፻")
    car = car.replace("፻0", "፲፻")
    car = car.replace("፲፻0", "፼")
    await message.answer(car)

executor.start_polling(dp)