# Keyboard Prank Project

The Keyboard Prank project is a fun and harmless prank application that can be used to surprise and amuse your friends. This project is designed to play a silly sound effect whenever a user types something on a target computer. The prank code is configured to start automatically with each reboot, ensuring that the surprise is repeated every time the computer restarts.

Please note that this prank is intended for entertainment purposes only and should only be used with the consent of the target individual. It's important to respect the privacy and boundaries of others while having a good laugh.

## Getting Started

Follow these instructions to set up the Keyboard Prank on the target computer:

1. **Clone the Repository**: Begin by cloning this repository onto the target computer using the following command:

    ```bash
    git clone https://github.com/aetricy/keyboard_prank.git
    ```
  
3.  **Operation System**: Depending on your friend's operating system, follow the appropriate installation instructions:



- **Linux Installation**

    ```bash
     chmod +x install.sh
     sudo ./install.sh
    ```

    
- **Windows Installation**:
   
   *Do not support windows yet.*

   
#### This will install and configure the prank to start on every reboot.

3. **Enjoy the Prank**: Sit back and watch the hilarity ensue as the target computer plays a silly sound effect every time the user types something.

---

## Customization

Feel free to customize the sound effect to your preference:

- **Sound Effect**: You can replace the default sound effect with your own preferred sound. Simply replace the `silly_sound.mp3` file in `sounds` directory


## Removal

If you decide to remove the prank from the target computer:

- Run the removal script:

### Linux

   ```bash
   sudo ./delete.sh
   ```

### Windows

   *Do not support windows yet.*


#### This will remove the prank from the system.


## Roadmap

- Windows Support

- Enhanced Sound Effect Triggers - Implement context-based and randomized triggers for added surprise.

- Sound Effect Library - Offer a variety of amusing sound options for enhanced pranking.

- Prank Scheduling - Schedule pranks to surprise at specific times or days.

- Mobile Control App - Enable remote prank activation and real-time reaction capture via a mobile app.

- Plug-and-Play Convenience - Simply plug the specially designed USB device into the target computer, and the fun begins immediately.


## Note

This prank application is meant to be light-hearted and fun. Always use it responsibly and with the consent of the target individual. Respect their privacy and avoid causing any inconvenience.

Happy pranking! 😄🎉

---

