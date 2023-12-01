from PyPDF2 import PdfFileReader, PdfFileWriter
from io import BytesIO
from reportlab.lib.pagesizes import letter, legal
from reportlab.pdfgen import canvas
import tensorflow as tf
from tensorflow import keras
import turtle

class CustomPdfEditor:
    def __init__(self, filename, page_size):
        self.pdf_reader = PdfFileReader(filename)
        self.page = self.pdf_reader.getPage(0)
        self.content_buffer = BytesIO()
        self.canvas = canvas.Canvas(self.content_buffer, pagesize=(letter if page_size == 'letter' else legal))

    def draw_string(self, x, y, content):
        self.canvas.drawString(x, y, content)

    def set_font_size(self, size):
        self.canvas.setFontSize(int(size))

    def save(self, output_filename):
        self.canvas.save()
        self.content_buffer.seek(0)
        text_pdf = PdfFileReader(self.content_buffer)
        

        output_pdf = PdfFileWriter()
        output_page = self.page.extract_text()  # Extract text content from the original page
    
        text_page = text_pdf.getPage(0)
        output_page.merge_page(text_page)
        
    
        output_pdf.add_page(output_page)
        
      
        with open(output_filename, 'wb') as output_stream:
            output_pdf.write(output_stream)

    def perform_machine_learning(self, text):
     
        model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(10,)),
            keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

     
        tensor_data = tf.constant([[ord(char) for char in text]])

        # Perform prediction using the model
        prediction = model.predict(tensor_data)
        print("Machine Learning Prediction:", prediction)

    def draw_square_with_turtle(self):
        turtle.speed(2)
        for _ in range(4):
            turtle.forward(100)
            turtle.right(90)
        turtle.done()

if __name__ == '__main__':
    
    editor = CustomPdfEditor('original.pdf', page_size='letter')
    editor.set_font_size(12)
    editor.draw_string(100, 100, 'Hello, World!')
    editor.save('modified.pdf')F.py
