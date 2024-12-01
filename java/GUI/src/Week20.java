import javax.swing.*;
import java.awt.*;

public class Week20 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Form");
        JLabel labelText = new JLabel("Form");
        labelText.setFont(new Font("Arial", Font.ITALIC, 30));
        JLabel labelName = new JLabel("Name");
        JLabel labelAge = new JLabel("Age");
        JButton button = new JButton("Button");
        button.setBackground(Color.orange);
        button.setBorder(BorderFactory.createEmptyBorder(15, 0, 15, 0));
        JTextField textFieldName = new JTextField();
        textFieldName.setColumns(20);
        JTextField textFieldAge = new JTextField();
        textFieldAge.setColumns(20);
        JPanel panelOne = new JPanel();
        panelOne.setBorder(BorderFactory.createEmptyBorder(30, 0, 30, 0));
        panelOne.setBackground(Color.CYAN);

        JPanel panelTwo = new JPanel();
        panelTwo.setBackground(Color.GREEN);
        panelOne.add(labelText);

        panelTwo.add(labelName);
        panelTwo.add(textFieldName);
        panelTwo.add(labelAge);
        panelTwo.add(textFieldAge);

        frame.add(panelOne, BorderLayout.PAGE_START);
        frame.add(panelTwo, BorderLayout.CENTER);
        frame.add(button, BorderLayout.PAGE_END);
        frame.setSize(500, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}