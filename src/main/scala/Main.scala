import org.apache.tika.Tika
import org.apache.tika.sax.BodyContentHandler
import org.apache.tika.metadata.Metadata
import java.io.FileInputStream
import java.io.File
import org.apache.tika.parser.pdf.PDFParser
import org.apache.tika.parser.ParseContext
import org.apache.tika.metadata.PDF
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths
import java.io.FileNotFoundException
import org.xml.sax.Attributes

object Main extends App {

  val handler = new BodyContentHandler()

  

  val metadata = new Metadata()

  // create a file stream 
  val inputstream = new FileInputStream(new File("/Users/danie/new_project_processing_diff_some_pdf_file/letter-booklet-2020-world-population.pdf"))
  
  // pass context information to tika parser
  val context = new ParseContext()

  val pdfparser = new PDFParser()
  pdfparser.parse(inputstream,handler,metadata,context)

  val content = handler.toString()
  val path = Paths.get("/Users/danie/new_project_processing_diff_some_pdf_file/example.txt")
  
  try {
    Files.write(path,content.getBytes())
  } catch {
    case e: FileNotFoundException => println("Couldn't find that file.")
  }
}