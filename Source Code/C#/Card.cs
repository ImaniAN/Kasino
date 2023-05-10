using System.Globalization;
using System.Threading;
using System;

public class Card
{
	public enum Face {ACE = 1, JACK = 11, QUEEN = 12, KING = 13};
	public enum Suit {CLUB, HEART, SPADE, DIAMOND};

	public Face face {get; private set;}
	public Suit suit {get; private set;}

	public Card (Face face, Suit suit) {
		this.face = face;
		this.suit = suit;
	}

	public override string ToString () {
		return face.ToString()[0] + SuitToUTFString();
	}

	public string SuitToUTFString() {
		switch (this.suit) {
			case Card.Suit.CLUB:
				return "♣";
			case Card.Suit.HEART:
				return "♡";
			case Card.Suit.SPADE:
				return "♠";
			case Card.Suit.DIAMOND:
				return "♢";
		}
		throw new System.Exception ("Not a valid suit.");
	}

	public string faceToString () {
		TextInfo textInfo = Thread.CurrentThread.CurrentCulture.TextInfo;
		return textInfo.ToTitleCase(textInfo.ToLower(face.ToString()));
	}

	public string suitToString () {
		TextInfo textInfo = Thread.CurrentThread.CurrentCulture.TextInfo;
		string s = textInfo.ToTitleCase(textInfo.ToLower(this.suit.ToString()));
		return s + "s";
	}
}
