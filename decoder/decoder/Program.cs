using System;

namespace decoder
{
    class Program
    {
        static void Main(string[] args)
        {
            string base64Encoded = "tZUgKSC8ukOgLdEb5riOQ=";
            string base64Decoded;
            byte[] data = System.Convert.FromBase64String(base64Encoded);
            base64Decoded = System.Text.ASCIIEncoding.ASCII.GetString(data);
            Console.WriteLine(base64Decoded);
        }
    }
}
