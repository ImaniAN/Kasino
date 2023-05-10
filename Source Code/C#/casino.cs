using System;
using System.Collections.Generic;
using System.Threading;

public class casino {
	public static int Main(string[] args)
	{
		List<Card> deck = DeckFactory.createDeck();
		foreach (Card c in deck) {
			Console.WriteLine(c);
		}
		return 0;
	}
}
