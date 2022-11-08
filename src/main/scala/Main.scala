import org.apache.tika.Tika
import org.apache.tika.sax.BodyContentHandler
import org.apache.tika.metadata.Metadata
import java.io.FileInputStream
import java.io.File
import org.apache.tika.parser.pdf.PDFParser
import org.apache.tika.parser.ParseContext
import org.apache.tika.metadata.PDF

object Main extends App {
  val handler = new BodyContentHandler()

  val metadata = new Metadata()

  // create a file stream 
  val inputstream = new FileInputStream(new File("https://www.censtatd.gov.hk/en/data/stat_report/product/B1120106/att/B11201062021XXXXB01.pdf"))
  
  // pass context information to tika parser
  val context = new ParseContext()

  val pdfparser = new PDFParser()
  pdfparser.parse(inputstream,handler,metadata,context)

  println(handler.toString())
}