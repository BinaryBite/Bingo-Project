from fpdf import FPDF

############################################################################################

class PDF(FPDF): #pdf class created to hold bingo cards
  def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Bingo Cards', 0, 1, 'C')

  def chapter_title(self, num, label):
      self.set_font('Arial', 'B', 12)
      self.cell(0, 10, 'Card %d: %s' % (num, label), 0, 1, 'L')
      self.ln(4)

  def chapter_body(self, body):
      self.set_font('Arial', '', 12)
      self.multi_cell(0, 10, body, align = "C")

def draw_bingo_cards(pdf, cards, image_address = None): #function that maps bingo card numpy arrays each on to an indiviual page of the pdf
    
    page_width = pdf.w
    naming = ["B","I","N","G","O"]
    
    for key, card in cards.items():
    
        pdf.add_page()
        
        rows, cols = card.shape
        
        #finds the centermost 5 columns to put the naming lists vairables into
        center = (cols // 2)
        header = [center -2, center - 1, center, center + 1, center + 2]
        
        cell_size = min(30, (pdf.w - 20) / cols) #ensures that the cells are appropriately sized to the page
        font_size = min(12, cell_size / 2) #ensures that the font also adheres to the cell sizing
        
        card_width = len(card[0]) * cell_size
        card_height = len(card) * cell_size
        
        #ensure that the bingo card isn't pinned to the leftmost side of the sheet

        offset_x = (page_width - card_width) / 2

        pdf.set_xy(pdf.get_x() + offset_x, pdf.get_y())

        pdf.set_font('Arial', 'B', font_size)
        
        for j in range(cols): #first iteration to put in the header for each bingo card
            
            pdf.rect(10 + j * cell_size, pdf.get_y(), cell_size, cell_size)
            
            pdf.set_xy(10 + j * cell_size, pdf.get_y() + 0.5 * cell_size)
            
            
            if j in header:
                pdf.cell(cell_size, 0, f"{naming[header.index(j)]}", align='C')
                
            pdf.set_xy(10 + j * cell_size, pdf.get_y() - 0.5 * cell_size)
            
        pdf.set_font('Arial', '', font_size)

        for i in range(rows): #following iterations for the actual bingo card

            pdf.set_xy(10, pdf.get_y() + cell_size)

            for j in range(cols):

                pdf.rect(10 + j*cell_size, pdf.get_y(), cell_size, cell_size)
                pdf.set_xy(10 + j*cell_size, pdf.get_y() + 0.5 * cell_size)
                
                if image_address is not None and card[i,j] == 0: #check to replace empty cells with image
                    pdf.image(image_address, pdf.get_x(), pdf.get_y() - 0.5 * cell_size, cell_size, cell_size)

                elif card[i, j] != 0:
                    pdf.cell(cell_size, 0, str(card[i, j]), align='C')

                pdf.set_xy(10 + j*cell_size, pdf.get_y() - 0.5 * cell_size)