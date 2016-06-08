// Taken from http://www.codeproject.com/Articles/11541/The-Simplest-C-Events-Example-Imaginable
using System;
namespace wildert
{

    // From https://msdn.microsoft.com/en-us/library/ak9w5846.aspx
    public interface ITickingThing
    {
        event EventHandler Tick;
    }

    public class Metronome
    {
        public event TickHandler Tick;
        public EventArgs e = null;
        public delegate void TickHandler(Metronome m, EventArgs e);
        public void Start()
        {
            while (true)
            {
                System.Threading.Thread.Sleep(3000);
                if (Tick != null)
                {
                    Tick(this, e);
                }
            }
        }
    }
        public class Listener
        {
            public void Subscribe(Metronome m)
            {
                m.Tick += new Metronome.TickHandler(HeardIt);
            }
            private void HeardIt(Metronome m, EventArgs e)
            {
                System.Console.WriteLine("HEARD IT");
            }

        }
    class Test
    {
        static void Main()
        {
            Metronome m = new Metronome();
            Listener l = new Listener();
            l.Subscribe(m);
            m.Start();
        }
    }
}
