# This is a sample Python script.
import multiprocessing
import subprocess

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def abaqus_verification(path):
    #    验证参数
    #    SUMMARY: verify executes the Abaqus installation verification
    #             procedure for one or more desired products.
    #      USAGE: abq6141 verify <options> [-log]
    #    OPTIONS: All options may be abbreviated with the shortest string
    #             that is unique. At least one option must be present.
    #    Common Options:
    #             -all         Run all product verification procedures
    #             -help        Display verification usage
    #             -install     Run installation verification procedures
    #             -log         Redirect verification output to a file named
    #                          "verify.log" in the current directory
    #    Product Options:
    #             -ams         Abaqus/AMS verification
    #             -tosca       Tosca For Abaqus verification
    #             -cae         Abaqus/CAE verification
    #             -cfd         Abaqus/CFD verification
    #             -design      Abaqus/Design verification
    #             -exp         Abaqus/Explicit verification
    #             -foundation  Abaqus/Foundation verification
    #             -param       Abaqus/Standard and Abaqus/Explicit parametric
    #                          studies verification
    #             -std         Abaqus/Standard verification
    #             -user_exp    Abaqus/Explicit with user subroutines verification
    #             -user_std    Abaqus/Standard with user subroutines verification
    #             -viewer      Abaqus/Viewer verification
    #    Translator Options:
    #             -adams       Abaqus Interface for MSC.ADAMS verification
    #             -catiav4     Geometry Translator for CATIA V4 verification
    #             -catiav5     Geometry Translator for CATIA V5 verification
    #             -dcatiav5    Verify Direct Geometry Import for CATIA V5 (verifies
    #                          geometry import capability in Abaqus/CAE; does not
    #                          verify installation or functionality of the CATIA V5
    #                          Associative Interface plug-in)
    #             -moldflow    Abaqus Interface for Moldflow verification
    #             -parasolid   Geometry Translator for Parasolid verification
    #             -proe        Verify Geometry Translator for Pro/ENGINEER (verifies
    #                          geometry import capability in Abaqus/CAE; does not
    #                          verify installation or functionality of the
    #                          Pro/ENGINEER Associative Interface plug-in)
    #             -swi         Verify Geometry Translator for SolidWorks (verifies
    #                          geometry import capability in Abaqus/CAE; does not
    #                          verify installation or functionality of the SolidWorks
    #                          Associative Interface plug-in)
    #     Additional Options:
    #             -contextHelp    Abaqus/CAE context-sensitive help verification
    #             -cPerf          Abaqus/CAE performance
    #             -docUrl         Abaqus Documentation verification
    #             -ioPerf         Abaqus I/O performance
    #             -make           Abaqus make utility verification
    #             -noGui          Abaqus noGUI (CAE/Viewer) verification
    #             -NoLicenseCheck Skips all license checks
    #             -parallel       Abaqus analyses using parallelization verification
    #             -scripting      Abaqus scripting interface verification
    #             -verbose        Display debugging information
    #             -retainFiles    Retain verification files
    #      NOTES: If the -install option is used, no other options are permitted.
    process = subprocess.Popen([path, '-verify', '-param', '-std', '-user_std'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(process.stdout.readline, b''):
        print(line.decode('utf-8'), end='')
    process.communicate()

def run_abaqus_cae(path):
    # Use a breakpoint in the code line below to debug your script.
    process = subprocess.Popen([path, 'cae', 'noGUI=./script.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # 实时输出子进程的输出
    for line in iter(process.stdout.readline, b''):
        print(line.decode('utf-8'), end='')
    # 等待子进程完成
    process.communicate()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    abaqus_path = 'D:\\software\\SIMULIA\\Abaqus\\Commands\\abq6144.bat'

    verification = multiprocessing.Process(target=abaqus_verification, args=(abaqus_path,))
    verification.start()
    verification.join()

    # abaqus = multiprocessing.Process(target=run_abaqus_cae, args=(abaqus_path,))
    # abaqus.start()
    # abaqus.join()