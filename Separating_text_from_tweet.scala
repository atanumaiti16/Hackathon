/**
  * Created by atanu on 11/14/16.
  */
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
import org.apache.spark.sql.SQLContext
import org.json4s.DefaultFormats

object Hackathon {
  def main(args: Array[String]): Unit = {


    implicit val formats = DefaultFormats
    val conf = new SparkConf().setMaster("local").setAppName("wordcount")
    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)

    val tweettable = sqlContext.read.json("/media/atanu/New Volume/Tweet-analysis/streamingData.json")
    tweettable.printSchema()
    val text2 = sqlContext.sql("SELECT text from election ").rdd
    text2.take(50).foreach(println)
    text2.saveAsTextFile("/media/atanu/New Volume1/Tweet-analysis2")

  }
}
