interface AccessToken {
	public boolean check_availability(String title);
	public boolean reserve_book(String title);
}

public class LibraryData {

	private class LibraryAccessToken implements AccessToken {

		private LibraryData library;
		private int a_counter = 3;
		private int r_counter = 1;

		LibraryAccessToken(LibraryData library_) {
			library = library_;
		}

		public boolean check_availability(String title) {
			if (a_counter > 0) {
				a_counter--;
				return library.check_availability(title);
			} else {
				System.out.println("No more availability queries allowed in this transaction!");
				return false;
			}
		}

		public boolean reserve_book(String title) {
			if (r_counter > 0) {
				r_counter--;
				return library.reserve_book(title);
			} else {
				System.out.println("No more reservation queries allowed in this transaction!");
				return false;
			}
		}
	}

	private boolean check_availability(String title) {
		return false;
	}

	private boolean reserve_book(String title) {
		return true;
	}

	public AccessToken login(String u, String p) {
		return new LibraryAccessToken(this);
    }
}
