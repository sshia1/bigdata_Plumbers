// Simulate Hadoop MapReduce algorithm in Python==>Scala, doing word count on Shakespeare.txt
//
// data_source              = file_read(data_file, start_line, end_line)...file=>list of string, terminated by '\n'
// record_stream            = TextInputFormat(data_source).................init stream of kvp=(index, line$)
// intermediate_data        = mapper(record_stream)........................stream of tokens: kvp=(word, 1)
// intermediate_data        = partitioner(intermediate_data)...............return output=input since only 1 mapper function
// sorted_intermediate_data = shuffle_and_sort(intermediate_data)..........sort intermediate data by key
// final_data               = reducer(sorted_intermediate_data)............final output: dictionary of word count
//
// CAVEAT: de-pluralization is implemented on a very limited scale, using dictionary
import scala.collection.mutable.ArrayBuffer
import scala.io.Source
import scala.util
import scala.collection.mutable.Map

object mapreducetest {
  var text_filename            = "/home/field/Downloads/temp.txt"
  var data_source              = ArrayBuffer[String]()
  var record_stream            = ArrayBuffer[(Int,String)]()
  var intermediate_data        = ArrayBuffer[(String,Int)]()
  var sorted_intermediate_data = ArrayBuffer[(String,Int)]()

  var final_data:Map[String,Int]=Map()


  def main(args: Array[String]) {
    println("Started mapreducetest()...")
    file_read()
    TextInputFormat()
    mapper()
    partitioner()
    shuffle_and_sort()
    reducer()
    println("END.")
  }

  def file_read() {
    println("file_read()")

    val filename = text_filename
    for (line <- Source.fromFile(filename).getLines)
      data_source += line
    println(data_source.size)
  }

  def TextInputFormat(): Unit = {
    println("TextInputFormat()")
    var i = 0
    var lineno = 0;
    var linestr = ""
    for(i <- 0 to (data_source.size - 1)) {
      lineno = i
      linestr = data_source(i)
      record_stream.append((lineno, linestr))
    }
  }

  def mapper(): Unit = {
    println("mapper()")
    var i = 0
    var j = 0
    var line = ""
    var key = ""
    var value=1
    for(i <- 0 to (record_stream.size - 1)) {
      line = record_stream(i)._2
      val wordlist = line.split(" ")
      for(i<-0 to (wordlist.size - 1)) {
        key=wordlist(i)
        value=1
        println(key, value)
        intermediate_data.append((key, value))
      }
    }
  }

  def partitioner(): Unit = {
    println("partitioner()")
    // stub, no change to intermediate data
    var i = 0
    for(i<-0 to (intermediate_data.size-1)) {
      println(intermediate_data(i)._1, intermediate_data(i)._2)
    }
  }

  def shuffle_and_sort(): Unit = {
    println("shuffle_and_sort()")
    //sorted_intermediate_data = scala.util.Sorting.stableSort(intermediate_data)
    sorted_intermediate_data = intermediate_data.sorted
    var i = 0
    for(i<-0 to (sorted_intermediate_data.size-1)) {
      println(sorted_intermediate_data(i)._1, intermediate_data(i)._2)
    }
  }

  def reducer(): Unit = {
    println("reducer()")
    var i = 0
    var key = ""
    var value = 0
    var contain = false
    for(i<-0 to (sorted_intermediate_data.size-1)){
      //final_data += sorted_interm
      //map.updateWith("a")({ case Some(count) => Some(count + 1) case None => Some(1) })
      key=sorted_intermediate_data(i)._1
      value=sorted_intermediate_data(i)._2
      println(final_data.contains(key))
      contain = final_data.contains(key)
      if (contain) {
        println("contain")
      }
      else {
        final_data = final_data + Map[String,Int](key->value)
      }


    }
  }
}
