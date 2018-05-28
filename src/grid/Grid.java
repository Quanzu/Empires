package grid;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class Grid extends Application
{

	public static void main(String[] args)
	{	
		launch(args);
	}


	@Override
	public void start(Stage stage) throws Exception 
	{
		BorderPane root = new BorderPane();
		Scene scene = new Scene(root, 400, 400);
		stage.setTitle("Empires");
		stage.setScene(scene);
		stage.show();
	}
}