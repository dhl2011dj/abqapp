import multiprocessing
import abaqus_interaction

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    verification = multiprocessing.Process(target=abaqus_interaction.verification, args=())
    verification.start()
    verification.join()

    abaqus = multiprocessing.Process(target=abaqus_interaction.run_cae, args=())
    abaqus.start()
    abaqus.join()