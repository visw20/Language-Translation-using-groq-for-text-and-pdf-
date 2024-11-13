# # import os
# from groq import Groq
# import time
# # import json

# class GroqTranslator:
#     def __init__(self, api_key=None):
#         # Directly use the provided API key
#         self.api_key = "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"
        
#         try:
#             self.client = Groq(api_key=self.api_key)
#             self.model = "llama3-70b-8192"
#         except Exception as e:
#             raise ValueError(f"Failed to initialize Groq client: {str(e)}")
        
#     def translate(self, text, source_lang, target_lang, max_retries=3):
#         """
#         Translate text using Groq API
#         """
#         prompt = f"""
#         Translate the following text from {source_lang} to {target_lang}.
#         Only return the translation, without any additional explanations.
        
#         Text to translate: {text}
        
#         Translation:
#         """
        
#         for attempt in range(max_retries):
#             try:
#                 completion = self.client.chat.completions.create(
#                     model=self.model,
#                     messages=[
#                         {"role": "system", "content": "You are a precise translator."},
#                         {"role": "user", "content": prompt}
#                     ],
#                     temperature=0.1,
#                     max_tokens=8192
#                 )
                
#                 return completion.choices[0].message.content.strip()
                
#             except Exception as e:
#                 if attempt == max_retries - 1:
#                     raise Exception(f"Translation failed after {max_retries} attempts: {str(e)}")
#                 time.sleep(1)
                
#     def batch_translate(self, texts, source_lang, target_lang):
#         """
#         Translate multiple texts in batch
#         """
#         translations = []
#         for text in texts:
#             translation = self.translate(text, source_lang, target_lang)
#             translations.append({
#                 'original': text,
#                 'translation': translation
#             })
#             time.sleep(0.5)
#         return translations

# def main():
#     try:
#         # Initialize translator without passing API key since it's hardcoded in the class
#         translator = GroqTranslator()
        
#         # Test single translation
#         text = """MS Dhoni: The Captain Cool of Indian Cricket

# Mahendra Singh Dhoni, widely known as MS Dhoni, is a legendary cricketer who has made an indelible mark on the history of Indian cricket. Born on July 7, 1981, in Ranchi, Jharkhand, Dhoni's journey from a small-town boy to one of the most successful and celebrated captains in the history of cricket is nothing short of inspiring. He rose to prominence through his fearless batting, exceptional leadership, and calm demeanor, earning the nickname "Captain Cool."

# Dhoni’s cricketing career began in 2004 when he made his debut for India in an ODI against Bangladesh. Initially, his aggressive batting style was met with skepticism, but his ability to adapt and perform under pressure quickly earned him a place in the team. His breakthrough moment came in 2005, when he scored an explosive 148 against Pakistan, a knock that put him on the cricketing map.

# Leadership Journey
# In 2007, Dhoni was given the responsibility of leading the Indian team for the inaugural ICC T20 World Cup. Under his leadership, India went on to win the tournament, an achievement that showcased his sharp cricketing acumen. This victory was just the beginning of Dhoni’s success as captain. His ability to inspire and lead by example was evident in every tournament he captained India in, and his strategic mind made him one of the most astute captains in cricket history.

# In 2008, Dhoni took over as captain of the Indian One Day International (ODI) and Test teams, following the retirement of Sourav Ganguly and the stepping down of Rahul Dravid. Under his leadership, India reached the pinnacle of international cricket, winning the 2007 ICC T20 World Cup, the 2011 ICC Cricket World Cup, and the 2013 ICC Champions Trophy. These victories solidified Dhoni’s legacy as one of the greatest captains ever to grace the game.

# Achievements
# ICC T20 World Cup (2007): One of Dhoni's most significant achievements was leading India to victory in the inaugural ICC T20 World Cup. The victory came at a time when T20 cricket was still emerging, and India's triumph served to establish Dhoni as a leader with a great vision for the future of Indian cricket.

# ICC Cricket World Cup (2011): The crowning achievement of Dhoni’s career was leading India to victory in the 2011 ICC Cricket World Cup. In the final against Sri Lanka, Dhoni played one of the most iconic knocks in Indian cricket history, scoring an unbeaten 91 runs and guiding his team to a historic win. This win marked the first time in 28 years that India had lifted the World Cup, and it was a fitting moment for Dhoni, who had captained the team to glory.

# ICC Champions Trophy (2013): Dhoni’s leadership also led India to victory in the 2013 ICC Champions Trophy, a tournament that brought together the best cricketing nations. India’s win in this tournament made Dhoni the first captain to win all three major ICC tournaments, cementing his place as one of the greatest captains in the history of the sport.

# Indian Premier League (IPL): Apart from international cricket, Dhoni's achievements in domestic T20 leagues, particularly the Indian Premier League (IPL), are worth mentioning. As captain of the Chennai Super Kings (CSK), Dhoni led the team to three IPL titles (2010, 2011, and 2018). His leadership, alongside his consistent performances with the bat and his ability to finish games, made him one of the most sought-after players in the IPL.

# Test Cricket: Dhoni’s leadership in Test cricket was equally impressive. Although he is often remembered for his limited-overs success, he was also a key figure in India’s rise to the top of the ICC Test rankings. Under his captaincy, India reached No. 1 in the ICC Test rankings for the first time in 2009.

# Leadership Style
# Dhoni’s leadership style is often described as calm, composed, and pragmatic. Unlike some of his contemporaries, who were more vocal and animated on the field, Dhoni was known for his silent and effective leadership. His ability to stay calm in high-pressure situations earned him the "Captain Cool" moniker. He was a leader who led by example, both on and off the field, always putting the team’s needs ahead of his own.

# Dhoni's decision-making was highly regarded, as he could read the game with great clarity. His innovative strategies, such as sending himself in to bat at crucial moments or giving unconventional bowlers the ball in tight situations, often paid off. His trust in his players and his ability to back them in difficult times made him a popular captain among his teammates.

# Personal Life
# Dhoni was a highly disciplined individual, balancing his cricketing career with his personal life. He married Sakshi Singh Rawat in 2010, and the couple has a daughter named Ziva. Despite his fame and success, Dhoni remained grounded and maintained a private life away from the media. His love for motorcycles and adventure sports was well known, and he often spent his downtime riding bikes and indulging in his hobbies.

# Dhoni’s philanthropic work is also noteworthy. He has supported various charitable causes, including promoting sports in rural areas and working with the Indian government to improve sports infrastructure.

# Retirement and Legacy
# In August 2020, Dhoni announced his retirement from international cricket, leaving the cricketing world in shock and sadness. His retirement marked the end of an era in Indian cricket. However, his legacy continues to inspire millions of aspiring cricketers. Dhoni’s ability to manage pressure, his remarkable leadership qualities, and his contribution to Indian cricket make him an immortal figure in the sport’s history.

# Dhoni's achievements and success story will be remembered for years to come. He not only transformed Indian cricket but also set a new standard for leadership, resilience, and determination. Today, MS Dhoni remains one of the most influential figures in the world of sports, a symbol of hard work, perseverance, and leadership.



             
#                    """
#         translation = translator.translate(text, "English", "French")
#         # print(f"\nSingle translation:")
#         print(f"Original: {text}")
#         print(f"Translation: {translation}")
        
#     except Exception as e:
#         print(f"Error: {str(e)}")

# if __name__ == "__main__":
#     main()






#for pdf


import os
from groq import Groq
import time
import json
import PyPDF2
from pathlib import Path
from fpdf import FPDF

class PDFTranslator:
    def __init__(self, api_key=None):
        self.api_key = "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"
        
        try:
            self.client = Groq(api_key=self.api_key)
            self.model = "gemma2-9b-it"
        except Exception as e:
            raise ValueError(f"Failed to initialize Groq client: {str(e)}")
    
    def extract_text_from_pdf(self, pdf_path):
        try:
            text_content = []
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text_content.append(page.extract_text())
            return '\n'.join(text_content)
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
    
    def translate_text(self, text, source_lang, target_lang, max_retries=3):
        chunks = [text[i:i+5000] for i in range(0, len(text), 5000)]
        translated_chunks = []
        
        for chunk in chunks:
            prompt = f"""
            Translate the following text from {source_lang} to {target_lang}.
            Only return the translation.
            
            Text to translate: {chunk}
            
            Translation:
            """
            
            for attempt in range(max_retries):
                try:
                    completion = self.client.chat.completions.create(
                        model=self.model,
                        messages=[
                            {"role": "system", "content": "You are a precise translator."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.3,
                        max_tokens=2000
                    )
                    translated_chunks.append(completion.choices[0].message.content.strip())
                    break
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise Exception(f"Translation failed after {max_retries} attempts: {str(e)}")
                    time.sleep(1)
        
        return '\n'.join(translated_chunks)
    
    def create_translated_pdf(self, translated_text, output_path):
        try:
            pdf = FPDF()
            pdf.add_page()
            
            pdf.add_font('DejaVu', '', 'C:/pdf to language transulation/dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf', uni=True)  # Adjust font path as needed
            pdf.set_font('DejaVu', '', 12)
            
            lines = translated_text.split('\n')
            for line in lines:
                pdf.multi_cell(0, 10, line)
            
            pdf.output(output_path)
        except Exception as e:
            raise Exception(f"Error creating PDF: {str(e)}")
    
    def translate_pdf(self, input_pdf_path, output_pdf_path, source_lang, target_lang):
        try:
            print(f"Reading PDF: {input_pdf_path}")
            original_text = self.extract_text_from_pdf(input_pdf_path)
            
            print(f"Translating from {source_lang} to {target_lang}...")
            translated_text = self.translate_text(original_text, source_lang, target_lang)
            
            print(f"Creating translated PDF: {output_pdf_path}")
            self.create_translated_pdf(translated_text, output_pdf_path)
            
            return True
        except Exception as e:
            print(f"Error during PDF translation: {str(e)}")
            return False

def main():
    try:
        translator = PDFTranslator()
        
        input_pdf = "C:/Users/Viswajith/Downloads/ChatBot Questions.pdf"
        output_pdf = "C:/Users/Viswajith/Downloads/translated_output1.pdf"
        
        success = translator.translate_pdf(
            input_pdf_path=input_pdf,
            output_pdf_path=output_pdf,
            source_lang="English",
            target_lang="French"
        )
        
        if success:
            print(f"Translation completed successfully!")
            print(f"Translated PDF saved as: {output_pdf}")
        else:
            print("Translation failed!")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()





#----------------------------





























